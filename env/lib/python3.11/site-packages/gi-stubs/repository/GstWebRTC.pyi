from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstSdp

_lock = ...  # FIXME Constant
_namespace: str = "GstWebRTC"
_version: str = "1.0"

def webrtc_error_quark() -> int: ...
def webrtc_sdp_type_to_string(type: WebRTCSDPType) -> str: ...

class WebRTCDTLSTransport(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCDTLSTransport(**properties)

    Object GstWebRTCDTLSTransport

    Properties from GstWebRTCDTLSTransport:
      session-id -> guint: Session ID
        Unique session ID
      transport -> GstWebRTCICETransport: ICE transport
        ICE transport used by this dtls transport
      state -> GstWebRTCDTLSTransportState: DTLS state
        State of the DTLS transport
      client -> gboolean: DTLS client
        Are we the client in the DTLS handshake?
      certificate -> gchararray: DTLS certificate
        DTLS certificate
      remote-certificate -> gchararray: Remote DTLS certificate
        Remote DTLS certificate

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        certificate: str
        client: bool
        remote_certificate: str
        session_id: int
        state: WebRTCDTLSTransportState
        transport: WebRTCICETransport
        name: Optional[str]
        parent: Optional[Gst.Object]
    props: Props = ...
    def __init__(
        self,
        certificate: str = ...,
        client: bool = ...,
        session_id: int = ...,
        name: Optional[str] = ...,
        parent: Gst.Object = ...,
    ): ...

class WebRTCDTLSTransportClass(GObject.GPointer): ...

class WebRTCDataChannel(GObject.Object):
    """
    :Constructors:

    ::

        WebRTCDataChannel(**properties)

    Object GstWebRTCDataChannel

    Signals from GstWebRTCDataChannel:
      on-open ()
      on-close ()
      on-error (GError)
      on-message-data (GBytes)
      on-message-string (gchararray)
      on-buffered-amount-low ()
      send-data (GBytes)
      send-string (gchararray)
      close ()

    Properties from GstWebRTCDataChannel:
      label -> gchararray: Label
        Data channel label
      ordered -> gboolean: Ordered
        Using ordered transmission mode
      max-packet-lifetime -> gint: Maximum Packet Lifetime
        Maximum number of milliseconds that transmissions and retransmissions may occur in unreliable mode (-1 = unset)
      max-retransmits -> gint: Maximum Retransmits
        Maximum number of retransmissions attempted in unreliable mode
      protocol -> gchararray: Protocol
        Data channel protocol
      negotiated -> gboolean: Negotiated
        Whether this data channel was negotiated by the application
      id -> gint: ID
        ID negotiated by this data channel (-1 = unset)
      priority -> GstWebRTCPriorityType: Priority
        The priority of data sent using this data channel
      ready-state -> GstWebRTCDataChannelState: Ready State
        The Ready state of this data channel
      buffered-amount -> guint64: Buffered Amount
        The amount of data in bytes currently buffered
      buffered-amount-low-threshold -> guint64: Buffered Amount Low Threshold
        The threshold at which the buffered amount is considered low and the buffered-amount-low signal is emitted

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffered_amount: int
        buffered_amount_low_threshold: int
        id: int
        label: str
        max_packet_lifetime: int
        max_retransmits: int
        negotiated: bool
        ordered: bool
        priority: WebRTCPriorityType
        protocol: str
        ready_state: WebRTCDataChannelState
    props: Props = ...
    def __init__(
        self,
        buffered_amount_low_threshold: int = ...,
        id: int = ...,
        label: str = ...,
        max_packet_lifetime: int = ...,
        max_retransmits: int = ...,
        negotiated: bool = ...,
        ordered: bool = ...,
        priority: WebRTCPriorityType = ...,
        protocol: str = ...,
    ): ...
    def close(self) -> None: ...
    def send_data(self, data: Optional[GLib.Bytes] = None) -> None: ...
    def send_string(self, str: Optional[str] = None) -> None: ...

class WebRTCDataChannelClass(GObject.GPointer): ...

class WebRTCICETransport(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCICETransport(**properties)

    Object GstWebRTCICETransport

    Signals from GstWebRTCICETransport:
      on-selected-candidate-pair-change ()
      on-new-candidate (gchararray)

    Properties from GstWebRTCICETransport:
      component -> GstWebRTCICEComponent: ICE component
        The ICE component of this transport
      state -> GstWebRTCICEConnectionState: ICE connection state
        The ICE connection state of this transport
      gathering-state -> GstWebRTCICEGatheringState: ICE gathering state
        The ICE gathering state of this transport

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        component: WebRTCICEComponent
        gathering_state: WebRTCICEGatheringState
        state: WebRTCICEConnectionState
        name: Optional[str]
        parent: Optional[Gst.Object]
    props: Props = ...
    def __init__(
        self,
        component: WebRTCICEComponent = ...,
        name: Optional[str] = ...,
        parent: Gst.Object = ...,
    ): ...

class WebRTCICETransportClass(GObject.GPointer): ...

class WebRTCRTPReceiver(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCRTPReceiver(**properties)

    Object GstWebRTCRTPReceiver

    Properties from GstWebRTCRTPReceiver:
      transport -> GstWebRTCDTLSTransport: Transport
        The DTLS transport for this receiver

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        transport: WebRTCDTLSTransport
        name: Optional[str]
        parent: Optional[Gst.Object]
    props: Props = ...
    def __init__(self, name: Optional[str] = ..., parent: Gst.Object = ...): ...

class WebRTCRTPReceiverClass(GObject.GPointer): ...

class WebRTCRTPSender(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCRTPSender(**properties)

    Object GstWebRTCRTPSender

    Properties from GstWebRTCRTPSender:
      priority -> GstWebRTCPriorityType: Priority
        The priority from which to set the DSCP field on packets
      transport -> GstWebRTCDTLSTransport: Transport
        The DTLS transport for this sender

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        priority: WebRTCPriorityType
        transport: WebRTCDTLSTransport
        name: Optional[str]
        parent: Optional[Gst.Object]
    props: Props = ...
    def __init__(
        self,
        priority: WebRTCPriorityType = ...,
        name: Optional[str] = ...,
        parent: Gst.Object = ...,
    ): ...
    def set_priority(self, priority: WebRTCPriorityType) -> None: ...

class WebRTCRTPSenderClass(GObject.GPointer): ...

class WebRTCRTPTransceiver(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCRTPTransceiver(**properties)

    Object GstWebRTCRTPTransceiver

    Properties from GstWebRTCRTPTransceiver:
      sender -> GstWebRTCRTPSender: Sender
        The RTP sender for this transceiver
      receiver -> GstWebRTCRTPReceiver: Receiver
        The RTP receiver for this transceiver
      current-direction -> GstWebRTCRTPTransceiverDirection: Current Direction
        Transceiver current direction
      direction -> GstWebRTCRTPTransceiverDirection: Direction
        Transceiver direction
      mlineindex -> guint: Media Line Index
        Index in the SDP of the Media
      mid -> gchararray: Media ID
        The media ID of the m-line associated with this transceiver. This  association is established, when possible, whenever either a local or remote description is applied. This field is null if neither a local or remote description has been applied, or if its associated m-line is rejected by either a remote offer or any answer.
      kind -> GstWebRTCKind: Media Kind
        Kind of media this transceiver transports

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        codec_preferences: Gst.Caps
        current_direction: WebRTCRTPTransceiverDirection
        direction: WebRTCRTPTransceiverDirection
        kind: WebRTCKind
        mid: str
        mlineindex: int
        receiver: WebRTCRTPReceiver
        sender: WebRTCRTPSender
        name: Optional[str]
        parent: Optional[Gst.Object]
    props: Props = ...
    def __init__(
        self,
        codec_preferences: Gst.Caps = ...,
        direction: WebRTCRTPTransceiverDirection = ...,
        mlineindex: int = ...,
        receiver: WebRTCRTPReceiver = ...,
        sender: WebRTCRTPSender = ...,
        name: Optional[str] = ...,
        parent: Gst.Object = ...,
    ): ...

class WebRTCRTPTransceiverClass(GObject.GPointer): ...

class WebRTCSCTPTransport(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCSCTPTransport(**properties)

    Object GstWebRTCSCTPTransport

    Properties from GstWebRTCSCTPTransport:
      transport -> GstWebRTCDTLSTransport: WebRTC DTLS Transport
        DTLS transport used for this SCTP transport
      state -> GstWebRTCSCTPTransportState: WebRTC SCTP Transport state
        WebRTC SCTP Transport state
      max-message-size -> guint64: Maximum message size
        Maximum message size as reported by the transport
      max-channels -> guint: Maximum number of channels
        Maximum number of channels

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        max_channels: int
        max_message_size: int
        state: WebRTCSCTPTransportState
        transport: WebRTCDTLSTransport
        name: Optional[str]
        parent: Optional[Gst.Object]
    props: Props = ...
    def __init__(self, name: Optional[str] = ..., parent: Gst.Object = ...): ...

class WebRTCSCTPTransportClass(GObject.GPointer): ...

class WebRTCSessionDescription(GObject.GBoxed):
    """
    :Constructors:

    ::

        WebRTCSessionDescription()
        new(type:GstWebRTC.WebRTCSDPType, sdp:GstSdp.SDPMessage) -> GstWebRTC.WebRTCSessionDescription
    """

    type: WebRTCSDPType = ...
    sdp: GstSdp.SDPMessage = ...
    def copy(self) -> WebRTCSessionDescription: ...
    def free(self) -> None: ...
    @classmethod
    def new(
        cls, type: WebRTCSDPType, sdp: GstSdp.SDPMessage
    ) -> WebRTCSessionDescription: ...

class WebRTCBundlePolicy(GObject.GEnum):
    BALANCED = 1
    MAX_BUNDLE = 3
    MAX_COMPAT = 2
    NONE = 0

class WebRTCDTLSSetup(GObject.GEnum):
    ACTIVE = 2
    ACTPASS = 1
    NONE = 0
    PASSIVE = 3

class WebRTCDTLSTransportState(GObject.GEnum):
    CLOSED = 1
    CONNECTED = 4
    CONNECTING = 3
    FAILED = 2
    NEW = 0

class WebRTCDataChannelState(GObject.GEnum):
    CLOSED = 4
    CLOSING = 3
    CONNECTING = 1
    NEW = 0
    OPEN = 2

class WebRTCError(GObject.GEnum):
    DATA_CHANNEL_FAILURE = 0
    DTLS_FAILURE = 1
    ENCODER_ERROR = 6
    FINGERPRINT_FAILURE = 2
    HARDWARE_ENCODER_NOT_AVAILABLE = 5
    INTERNAL_FAILURE = 8
    INVALID_STATE = 7
    SCTP_FAILURE = 3
    SDP_SYNTAX_ERROR = 4
    @staticmethod
    def quark() -> int: ...

class WebRTCFECType(GObject.GEnum):
    NONE = 0
    ULP_RED = 1

class WebRTCICEComponent(GObject.GEnum):
    RTCP = 1
    RTP = 0

class WebRTCICEConnectionState(GObject.GEnum):
    CHECKING = 1
    CLOSED = 6
    COMPLETED = 3
    CONNECTED = 2
    DISCONNECTED = 5
    FAILED = 4
    NEW = 0

class WebRTCICEGatheringState(GObject.GEnum):
    COMPLETE = 2
    GATHERING = 1
    NEW = 0

class WebRTCICERole(GObject.GEnum):
    CONTROLLED = 0
    CONTROLLING = 1

class WebRTCICETransportPolicy(GObject.GEnum):
    ALL = 0
    RELAY = 1

class WebRTCKind(GObject.GEnum):
    AUDIO = 1
    UNKNOWN = 0
    VIDEO = 2

class WebRTCPeerConnectionState(GObject.GEnum):
    CLOSED = 5
    CONNECTED = 2
    CONNECTING = 1
    DISCONNECTED = 3
    FAILED = 4
    NEW = 0

class WebRTCPriorityType(GObject.GEnum):
    HIGH = 4
    LOW = 2
    MEDIUM = 3
    VERY_LOW = 1

class WebRTCRTPTransceiverDirection(GObject.GEnum):
    INACTIVE = 1
    NONE = 0
    RECVONLY = 3
    SENDONLY = 2
    SENDRECV = 4

class WebRTCSCTPTransportState(GObject.GEnum):
    CLOSED = 3
    CONNECTED = 2
    CONNECTING = 1
    NEW = 0

class WebRTCSDPType(GObject.GEnum):
    ANSWER = 3
    OFFER = 1
    PRANSWER = 2
    ROLLBACK = 4
    @staticmethod
    def to_string(type: WebRTCSDPType) -> str: ...

class WebRTCSignalingState(GObject.GEnum):
    CLOSED = 1
    HAVE_LOCAL_OFFER = 2
    HAVE_LOCAL_PRANSWER = 4
    HAVE_REMOTE_OFFER = 3
    HAVE_REMOTE_PRANSWER = 5
    STABLE = 0

class WebRTCStatsType(GObject.GEnum):
    CANDIDATE_PAIR = 11
    CERTIFICATE = 14
    CODEC = 1
    CSRC = 6
    DATA_CHANNEL = 8
    INBOUND_RTP = 2
    LOCAL_CANDIDATE = 12
    OUTBOUND_RTP = 3
    PEER_CONNECTION = 7
    REMOTE_CANDIDATE = 13
    REMOTE_INBOUND_RTP = 4
    REMOTE_OUTBOUND_RTP = 5
    STREAM = 9
    TRANSPORT = 10
