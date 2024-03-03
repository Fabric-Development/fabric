import gi
from loguru import logger
from fabric.service import *
from fabric.utils import bulk_connect


class CvcImportError(ImportError):
    def __init__(self, *args):
        super().__init__(
            "Cvc is not installed, please install it first, you can use automated installer in the git repository",
            *args,
        )


try:
    gi.require_version("Cvc", "1.0")
    from gi.repository import Cvc
except:
    raise CvcImportError()


class AudioStream(Service):
    __gsignals__ = SignalContainer(
        Signal("changed", "run-first", None, ()),
        Signal("closed", "run-first", None, ()),
    )

    def __init__(
        self,
        stream: Cvc.MixerStream,
        control: Cvc.MixerControl,
        owener: object,
        **kwargs,
    ):
        self._stream = stream
        self._control = control
        self._owner = owener
        self._signal_connectors: dict = {}
        for sn in [
            "application-id",
            "description",
            "icon-name",
            "is-muted",
            "volume",
            "state",
            "id",
        ]:  # A PYRAMID
            self._signal_connectors[sn] = self._stream.connect(
                f"notify::{sn}", lambda *args, sn=sn: self.notifier(sn, args)
            )
            #                                  ^^^^^ python bug, i guess.
        self._old_vol = 0
        super().__init__(**kwargs)

    @Property(value_type=str, flags="readable")
    def icon_name(self) -> str:
        return self._stream.props.icon_name

    @Property(value_type=str, flags="readable")
    def name(self) -> str:
        return self._stream.props.name

    @Property(value_type=int, flags="readable")
    def id(self) -> int:
        return self._stream.props.id

    @Property(value_type=str, flags="readable")
    def icon(self) -> str:
        return self._stream.props.icon_name

    @Property(value_type=str, flags="readable")
    def description(self) -> str:
        return self._stream.props.description

    @Property(value_type=str, flags="readable")
    def application_id(self) -> str:
        return self._stream.props.application_id

    @Property(value_type=str, flags="readable")
    def state(self) -> str:
        return {
            Cvc.MixerStreamState.INVALID: "invalid",
            Cvc.MixerStreamState.RUNNING: "running",
            Cvc.MixerStreamState.IDLE: "idle",
            Cvc.MixerStreamState.SUSPENDED: "suspended",
        }.get(self._stream.props.state, "unknown")

    @Property(value_type=str, flags="readable")
    def control_state(self) -> str:
        return {
            Cvc.MixerControlState.CLOSED: "closed",
            Cvc.MixerControlState.READY: "ready",
            Cvc.MixerControlState.CONNECTING: "connecting",
            Cvc.MixerControlState.FAILED: "failed",
        }.get(self._control.props.state, "unknown")

    @Property(value_type=object, flags="readable")
    def stream(self) -> Cvc.MixerStream:
        return self._stream

    @Property(value_type=float, flags="read-write")
    def volume(self) -> float:
        return float(
            (self._stream.props.volume / self._control.get_vol_max_norm()) * 100
        )

    @volume.setter
    def volume(self, value: float):
        value = 0 if value < 0 else value
        value = self._owner.max_volume if value > self._owner.max_volume else value
        self._old_vol = self._stream.props.volume
        self._stream.set_volume((value * self._control.get_vol_max_norm()) / 100)
        self._stream.push_volume()
        self.emit("changed")
        return

    @Property(value_type=bool, default_value=False, flags="read-write")
    def is_muted(self) -> bool:
        return self._stream.props.is_muted

    @is_muted.setter
    def is_muted(self, value: bool):
        self._stream.set_is_muted(value)
        self._stream.change_is_muted(value)
        self.emit("changed")
        return

    def notifier(self, name: str, args):
        self.notify(name)
        self.emit("changed")
        return

    def close(self):
        for id in self._signal_connectors.values():
            try:
                self.stream.disconnect(id)
            except:
                pass
        self.emit("closed")

    def __del__(self):
        # hacking into the guts of python's garbage collector
        return self.close()


class Audio(Service):
    __gsignals__ = SignalContainer(
        Signal("changed", "run-first", None, ()),
        Signal("speaker-changed", "run-first", None, ()),
        Signal("microphone-changed", "run-first", None, ()),
        Signal("stream-added", "run-first", None, ()),
        Signal("stream-removed", "run-first", None, ()),
    )

    def __init__(
        self,
        controler_name: str = "fabric audio control",
        max_volume: int = 100,
        **kwargs,
    ):
        self._control = Cvc.MixerControl(name=controler_name)
        self._max_volume = max_volume
        self._streams: dict[AudioStream:int] = {}
        self._stream_connectors: dict[AudioStream:int] = {}
        self._speaker: AudioStream = None
        self._speaker_connection: SignalConnection = None
        self._microphone: AudioStream = None
        self._microphone_connection: SignalConnection = None
        bulk_connect(
            self._control,
            {
                "default-sink-changed": lambda _, id: self.on_default_io_changed(
                    id, "speaker"
                ),
                "default-source-changed": lambda _, id: self.on_default_io_changed(
                    id, "microphone"
                ),
                "stream-added": self.on_stream_added,
                "stream-removed": self.on_stream_removed,
            },
        )
        self._control.open()
        super().__init__(**kwargs)

    @Property(value_type=object, flags="readable")
    def speaker(self) -> AudioStream:
        return self._speaker

    @Property(value_type=object, flags="readable")
    def speakers(self) -> list[AudioStream]:
        return self.get_streams(Cvc.MixerSink)

    @Property(value_type=object, flags="readable")
    def microphone(self) -> AudioStream:
        return self._microphone

    @Property(value_type=object, flags="readable")
    def microphones(self) -> list[AudioStream]:
        return self.get_streams(Cvc.MixerSource)

    @Property(value_type=object, flags="readable")
    def applications(self) -> list[AudioStream]:
        return self.get_streams(Cvc.MixerSinkInput)

    @Property(value_type=object, flags="readable")
    def recorders(self) -> list[AudioStream]:
        return self.get_streams(Cvc.MixerSourceOutput)

    @Property(value_type=int, flags="read-write")
    def max_volume(self) -> int:
        return self._max_volume

    @max_volume.setter
    def max_volume(self, value: int):
        self._max_volume = value
        return

    @property
    def state(self) -> str:
        return {
            Cvc.MixerControlState.CLOSED: "closed",
            Cvc.MixerControlState.READY: "ready",
            Cvc.MixerControlState.CONNECTING: "connecting",
            Cvc.MixerControlState.FAILED: "failed",
        }.get(self._control.props.state, "unknown")

    def get_streams(
        self,
        stream_type: Cvc.MixerSource
        | Cvc.MixerSink
        | Cvc.MixerSinkInput
        | Cvc.MixerSourceOutput
        | None,
    ) -> list[AudioStream]:
        return (
            [x for x in self._streams.values() if isinstance(x._stream, stream_type)]
            if stream_type is not None
            else self._streams.values()
        )

    def on_default_io_changed(self, id: int, type: str):
        logger.info(f"[Audio][{type}] Changing default {type} to {id}")
        if self.__getattribute__(f"_{type}") is not None:
            logger.info(f"[Audio][{type}] Removing old {type} stream")
            try:
                self.__getattribute__(f"_{type}").disconnect(
                    self.__getattribute__(f"_{type}_connection")
                )
            except Exception as e:
                logger.warning(
                    f"[Audio] tried to remove a stream of type {type} but failed because of error ({e}), skipping..."
                )
        strm = self._streams.get(id)
        if strm is None:
            return
        self.__setattr__(f"_{type}", strm)
        bind = strm.connect("changed", lambda *args: self.emit(f"{type}-changed"))
        self.__setattr__(f"_{type}_connection", bind)
        self.emit("changed")
        self.emit(f"{type}-changed")
        self.notify(type)
        return

    def on_stream_removed(self, mixer_stream: Cvc.MixerStream, id: int):
        logger.info(f"[Audio] Removing stream with id {id}")
        strm = (
            self._control.lookup_stream_id(id)
            or self._control.lookup_output_id(id)
            or self._control.lookup_input_id(id)
        )
        if strm is None:
            return
        if self._streams.get(id) is None:
            return
        self._stream_connectors.get(id).disconnect()
        self._streams.pop(id)
        self._stream_connectors.pop(id)
        try:
            strm.close()
        except:
            pass
        self.emit("changed")

    def on_stream_added(self, ctrl: Cvc.MixerControl, id: int):
        if self._streams.get(id) is not None:
            return
        strm = self._control.lookup_stream_id(id)
        adstrm = AudioStream(strm, self._control, self)
        bind = adstrm.connect("changed", lambda *args: self.emit("changed"))
        self._streams[id] = adstrm
        self._stream_connectors[id] = bind
        self.emit("changed")
        return
