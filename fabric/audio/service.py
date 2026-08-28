import gi
from loguru import logger
from typing import Literal
from fabric.core.service import Service, Signal, Property
from fabric.utils import bulk_connect, get_enum_member_name, snake_case_to_kebab_case


class CvcImportError(ImportError):
    def __init__(self, *args):
        super().__init__(
            (
                "Cvc is not installed, please install it first, a common fix could be installing the cinnamon-desktop package (this is not the actual desktop environment, just a bunch of helper libraries.)\n"
                "if the cinnamon-desktop package is not available for you, we do have an automated installer in fabric's git repository."
            ),
            *args,
        )


try:
    gi.require_version("Cvc", "1.0")
    from gi.repository import Cvc
except Exception:
    raise CvcImportError()


class AudioStream(Service):
    """
    A class representing a stream of audio (i.e. speakers, microphones, applications and recorders)

    This class also enables the control of the contained stream (e.g. volume and mute state)
    """

    @Signal
    def changed(self) -> None: ...

    @Signal
    def closed(self) -> None: ...

    # TODO: implement a interface for getting the icon as a Gdk.Pixbuf (from stream.get_gicon())
    @Property(str, "readable")
    def icon_name(self) -> str:
        """A suggested icon name for this stream type

        :rtype: str
        """
        return self._stream.get_icon_name()

    @Property(int, "readable")
    def id(self) -> int:
        """The identifier of this stream

        :rtype: int
        """
        return self._stream.get_id()

    @Property(str, "readable")
    def name(self) -> str:
        """The display name associated with this stream

        :rtype: str
        """
        return self._stream.get_name()

    @Property(str, "readable")
    def description(self) -> str:
        """Text descriping this stream's purpose

        :rtype: str
        """
        return self._stream.get_description()

    @Property(str, "readable")
    def application_id(self) -> str:
        """This stream's application's identifier (if any)

        :rtype: str
        """
        return self._stream.get_application_id()

    @Property(str, "readable")
    def state(self) -> str:
        """The state this stream is currently in

        :rtype: str
        """
        return snake_case_to_kebab_case(
            get_enum_member_name(self._stream.get_state(), default="unknown")
        )

    @Property(Cvc.MixerStream, "readable")
    def stream(self) -> Cvc.MixerStream:
        """The actual stream object this class is holding

        :rtype: Cvc.MixerStream
        """
        return self._stream

    @Property(float, "read-write")
    def volume(self) -> float:
        """The current volume value for this stream (limited to parent's `max_volume`)

        :rtype: float
        """
        return float(
            (self._stream.props.volume / self._control.get_vol_max_norm()) * 100
        )

    @volume.setter
    def volume(self, value: float):
        value = 0 if value < 0 else value
        value = self._parent.max_volume if value > self._parent.max_volume else value
        self._old_vol = self._stream.props.volume
        self._stream.set_volume(int((value * self._control.get_vol_max_norm()) / 100))
        self._stream.push_volume()  # type: ignore
        return self.changed()

    @Property(bool, "read-write", "is-muted", default_value=False)
    def muted(self) -> bool:
        """Whether this stream is in a mute state currently or not

        :rtype: bool
        """
        return self._stream.get_is_muted()

    @muted.setter
    def muted(self, value: bool):
        self._stream.set_is_muted(value)
        self._stream.change_is_muted(value)  # type: ignore
        return self.changed()

    @Property(str, "readable")
    def type(self) -> str:
        return Audio.get_stream_type(self.stream, default="unknown")  # type: ignore

    def __init__(
        self,
        stream: Cvc.MixerStream,
        control: Cvc.MixerControl,
        parent: "Audio",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._old_vol = 0
        self._stream = stream
        self._control = control
        self._parent = parent
        for sn in [
            "application-id",
            "description",
            "icon-name",
            "is-muted",
            "volume",
            "state",
            "id",
        ]:  # A PYRAMID
            self._stream.connect(
                f"notify::{sn}", lambda *args, sn=sn: self.notifier(sn, args)
            )
            #                                  ^^^^^ python bug, i guess.

    def notifier(self, name: str, *args):
        self.notify(name)
        self.changed()
        return

    def close(self):
        return self.closed()

    def __del__(self):
        # hacking into the guts of python's garbage collector
        return self.close()


# TODO: cleanup a little bit more...
class Audio(Service):
    @Signal
    def changed(self) -> None: ...
    @Signal
    def speaker_changed(self) -> None: ...
    @Signal
    def microphone_changed(self) -> None: ...
    @Signal
    def stream_added(self) -> None: ...
    @Signal
    def stream_removed(self) -> None: ...

    @Property(AudioStream, "readable")
    def speaker(self) -> AudioStream:
        """The default speaker stream begin currently in use (if any)

        :rtype: AudioStream
        """
        return self._speaker

    @Property(list[AudioStream], "readable")
    def speakers(self) -> list[AudioStream]:
        """A list of all speaker streams connected to this device

        :rtype: list[AudioStream]
        """
        return self.do_list_stream_type(Cvc.MixerSink)

    @Property(AudioStream, "readable")
    def microphone(self) -> AudioStream:
        """The default microphone stream (if any)

        :rtype: AudioStream
        """
        return self._microphone

    @Property(list[AudioStream], "readable")
    def microphones(self) -> list[AudioStream]:
        """A list of all microphone streams connected to this device

        :rtype: list[AudioStream]
        """
        return self.do_list_stream_type(Cvc.MixerSource)

    @Property(list[AudioStream], "readable")
    def applications(self) -> list[AudioStream]:
        """A list of all application streams outputing audio at the moment

        :rtype: list[AudioStream]
        """
        return self.do_list_stream_type(Cvc.MixerSinkInput)

    @Property(list[AudioStream], "readable")
    def recorders(self) -> list[AudioStream]:
        """A list of application streams recording audio at the moment

        :rtype: list[AudioStream]
        """
        return self.do_list_stream_type(Cvc.MixerSourceOutput)

    @Property(int, "read-write")
    def max_volume(self) -> int:
        """The maximum volume value all streams can reach by setting the volume through **this service**

        :rtype: int
        """
        return self._max_volume

    @max_volume.setter
    def max_volume(self, value: int):
        self._max_volume = value
        return

    @Property(str, "readable")
    def state(self) -> str:
        return snake_case_to_kebab_case(
            get_enum_member_name(self._control.get_state(), default="unknown")
        )

    def __init__(
        self,
        max_volume: int = 100,
        controller_name: str = "fabric audio control",
        **kwargs,
    ):
        """
        :param max_volume: default maximum volume for all streams, this limit only works if volume setting is done through this service, defaults to 100
        :type max_volume: int, optional
        :param controller_name: the name of this service's mixer controll, defaults to "fabric audio control"
        :type controller_name: str, optional
        """
        super().__init__(**kwargs)
        self._control = Cvc.MixerControl(name=controller_name)
        self._max_volume = max_volume

        self._streams: dict[int, AudioStream] = {}
        self._stream_connectors: dict[int, int] = {}

        self._speaker: AudioStream | None = None
        self._speaker_connection: int | None = None

        self._microphone: AudioStream | None = None
        self._microphone_connection: int | None = None

        bulk_connect(
            self._control,
            {
                "stream-added": self.on_stream_added,
                "stream-removed": self.on_stream_removed,
                "default-sink-changed": lambda _, id: self.on_default_stream_changed(
                    id, "speaker"
                ),
                "default-source-changed": lambda _, id: self.on_default_stream_changed(
                    id, "microphone"
                ),
            },
        )

        # all aboard...
        self._control.open()

    def do_list_stream_type(
        self,
        stream_type: Literal[
            "source",
            "source-output",
            "sink",
            "sink-input",
        ]
        | type[Cvc.MixerSource]
        | type[Cvc.MixerSourceOutput]
        | type[Cvc.MixerSink]
        | type[Cvc.MixerSinkInput]
        | None = None,
    ) -> list[AudioStream]:
        if not stream_type:
            return list(self._streams.values())

        # get_enum_member won't help here :P
        stream_type = (
            {
                "source": Cvc.MixerSource,
                "source-output": Cvc.MixerSourceOutput,
                "sink": Cvc.MixerSink,
                "sink-input": Cvc.MixerSinkInput,
            }.get(stream_type)
            if isinstance(stream_type, str)
            else stream_type
        )

        rlist = []
        for _, strm in self._streams.items():
            if not stream_type or not isinstance(strm.stream, stream_type):
                continue
            rlist.append(strm)
        return rlist

    def on_default_stream_changed(self, id: int, type: str):
        logger.info(f"[Audio][{type.title()}] Changing default {type} to {id}")

        if (old_strm := self.__getattribute__(f"_{type}")) is not None:
            logger.info(f"[Audio][{type.title()}] Removing old {type} stream")
            try:
                hndlr_id = self.__getattribute__(f"_{type}_connection")
                old_strm.handler_disconnect(hndlr_id)
            except Exception as e:
                logger.warning(
                    f"[Audio][{type.title()}] tried to remove a stream of type {type} but failed because of error ({e}), skipping..."
                )

        strm = self._streams.get(id)
        if not strm:
            return

        self.__setattr__(f"_{type}", strm)
        self.__setattr__(
            f"_{type}_connection",
            strm.connect("changed", lambda *args: self.emit(f"{type}-changed")),
        )

        self.emit(f"{type}-changed")
        self.notify(type)

        return self.changed()

    def on_stream_added(self, _, stream_id: int):
        stream = (
            self._control.lookup_stream_id(stream_id)
            or self._control.lookup_output_id(stream_id)
            or self._control.lookup_input_id(stream_id)
        )

        if (
            self._streams.get(stream_id) is not None
            or not Audio.get_stream_type(stream, None)  # type: ignore
            or not stream
        ):
            return  # do not add it twice

        audio_stream = AudioStream(stream, self._control, self)
        self._streams[stream_id] = audio_stream
        self._stream_connectors[stream_id] = audio_stream.connect(
            "changed", lambda *_: self.changed()
        )

        logger.info(
            f"[Audio][{audio_stream.type.title()}] Adding stream {stream_id} with name {audio_stream.name}"
        )
        self.do_notify_streams(stream)
        return self.changed()

    def on_stream_removed(self, _, stream_id: int):
        if not self._streams.get(stream_id):
            return

        audio_stream = self._streams.pop(stream_id)
        audio_stream.handler_disconnect(self._stream_connectors.pop(stream_id))  # type: ignore

        logger.info(
            f"[Audio][{audio_stream.type.title()}] Removing stream {stream_id} with name {audio_stream.name}"
        )
        self.do_notify_streams(audio_stream.stream)
        audio_stream.close()
        return self.changed()

    def do_notify_streams(self, stream: Cvc.MixerStream):
        stream_type = Audio.get_stream_type(stream)
        if not stream_type:
            return
        return self.notify(stream_type)

    @staticmethod
    def get_stream_type(
        stream: Cvc.MixerStream,
        default=None,
    ) -> str | None:
        # intended for internal usage only
        return {
            Cvc.MixerSink: "speakers",
            Cvc.MixerSinkInput: "applications",
            Cvc.MixerSource: "microphones",
            Cvc.MixerSourceOutput: "recorders",
        }.get(type(stream), default)  # type: ignore
