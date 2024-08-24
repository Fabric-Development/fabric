import unittest
from fabric.core import Service, Signal


class TestServiceSignals(unittest.TestCase):
    class ServiceWithSignals(Service):
        int_signal = Signal("int-signal", "run-first", None, (int,))
        str_signal = Signal("str-signal", "run-first", None, (str,))
        bool_signal = Signal("bool-signal", "run-first", None, (bool,))
        boxed_signal = Signal("boxed-signal", "run-first", None, (object,))

        @Signal
        def complex_signal(
            self, intValue: int, strValue: str, boolValue: bool, boxedObject: object
        ):
            return "signalCalled"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def testOrphaned(self):
        int_signal = Signal("int-signal", "run-first", None, (int,))
        str_signal = Signal("str-signal", "run-first", None, (str,))
        bool_signal = Signal("bool-signal", "run-first", None, (bool,))
        boxed_signal = Signal("boxed-signal", "run-first", None, (object,))

        @Signal
        def complex_signal(
            self, strValue: str, intValue: int, boolValue: bool, boxedObject: object
        ): ...

    def testServiceSignalsConnect1(self):
        service = self.ServiceWithSignals()
        service.connect("int-signal", lambda *args: ...)
        service.connect("str-signal", lambda *args: ...)
        service.connect("bool-signal", lambda *args: ...)
        service.connect("boxed-signal", lambda *args: ...)
        service.connect("complex-signal", lambda *args: ...)

    def testServiceSignalsConnect2(self):
        self.ServiceWithSignals(
            on_int_signal=lambda *args: ...,
            on_str_signal=lambda *args: ...,
            on_bool_signal=lambda *args: ...,
            on_boxed_signal=lambda *args: ...,
            on_complex_signal=lambda *args: ...,
        )

    def testServiceSignalsConnect3(self):
        service = self.ServiceWithSignals()
        service.int_signal.connect(lambda *args: ...)
        service.str_signal.connect(lambda *args: ...)
        service.bool_signal.connect(lambda *args: ...)
        service.boxed_signal.connect(lambda *args: ...)
        service.complex_signal.connect(lambda *args: ...)

    def testServiceSignalsEmit1(self):
        service = self.ServiceWithSignals()
        service.emit("int-signal", 42)
        service.emit("str-signal", "42")
        service.emit("bool-signal", True)
        service.emit("boxed-signal", object)
        service.emit("complex-signal", 42, "42", True, object)

    def testServiceSignalsEmit2(self):
        service = self.ServiceWithSignals()
        service.int_signal.emit(42)
        service.str_signal.emit("42")
        service.bool_signal.emit(True)
        service.boxed_signal.emit(object)
        service.complex_signal.emit(42, "42", True, object)

    def testServiceSignalsEmit3(self):
        service = self.ServiceWithSignals()
        service.int_signal(42)
        service.str_signal("42")
        service.bool_signal(True)
        service.boxed_signal(object)
        service.complex_signal(42, "42", True, object)

    def testServiceSignalsConnectAndEmit1(self):
        emittedSignals: list[str] = []
        expectedOutput = [
            "int-signal",
            "str-signal",
            "bool-signal",
            "boxed-signal",
            "complex-signal",
        ]

        def onSignal(signalName):
            emittedSignals.append(signalName)

        service = self.ServiceWithSignals()
        service.connect("int-signal", lambda *args: onSignal("int-signal"))
        service.connect("str-signal", lambda *args: onSignal("str-signal"))
        service.connect("bool-signal", lambda *args: onSignal("bool-signal"))
        service.connect("boxed-signal", lambda *args: onSignal("boxed-signal"))
        service.connect("complex-signal", lambda *args: onSignal("complex-signal"))

        service.emit("int-signal", 42)
        service.emit("str-signal", "42")
        service.emit("bool-signal", True)
        service.emit("boxed-signal", object)
        service.emit("complex-signal", 42, "42", True, object)

        self.assertEqual(emittedSignals, expectedOutput)
        emittedSignals = []

    def testServiceSignalsConnectAndEmit2(self):
        emittedSignals: list[str] = []
        expectedOutput = [
            "int-signal",
            "str-signal",
            "bool-signal",
            "boxed-signal",
            "complex-signal",
        ]

        def onSignal(signalName):
            emittedSignals.append(signalName)

        service = self.ServiceWithSignals()
        service.int_signal.connect(lambda *args: onSignal("int-signal"))
        service.str_signal.connect(lambda *args: onSignal("str-signal"))
        service.bool_signal.connect(lambda *args: onSignal("bool-signal"))
        service.boxed_signal.connect(lambda *args: onSignal("boxed-signal"))
        service.complex_signal.connect(lambda *args: onSignal("complex-signal"))

        service.int_signal(42)
        service.str_signal("42")
        service.bool_signal(True)
        service.boxed_signal(object)
        service.complex_signal(42, "42", True, object)

        self.assertEqual(emittedSignals, expectedOutput)
        emittedSignals = []

    def testServiceSignalsConnectAndEmit3(self):
        emittedSignals: list[str] = []
        expectedOutput = [
            "int-signal",
            "str-signal",
            "bool-signal",
            "boxed-signal",
            "complex-signal",
        ]

        def onSignal(signalName):
            emittedSignals.append(signalName)

        service = self.ServiceWithSignals()

        service.int_signal.connect(lambda *args: onSignal("int-signal"))
        service.str_signal.connect(lambda *args: onSignal("str-signal"))
        service.bool_signal.connect(lambda *args: onSignal("bool-signal"))
        service.boxed_signal.connect(lambda *args: onSignal("boxed-signal"))
        service.complex_signal.connect(lambda *args: onSignal("complex-signal"))

        service.int_signal.emit(42)
        service.str_signal.emit("42")
        service.bool_signal.emit(True)
        service.boxed_signal.emit(object)
        service.complex_signal.emit(42, "42", True, object)

        self.assertEqual(emittedSignals, expectedOutput)
        emittedSignals = []

    def testServiceSignalsConnectAndEmit4(self):
        emittedSignals: list[str] = []
        expectedOutput = [
            "int-signal",
            "str-signal",
            "bool-signal",
            "boxed-signal",
            "complex-signal",
        ]

        def onSignal(signalName):
            emittedSignals.append(signalName)

        service = self.ServiceWithSignals(
            on_int_signal=lambda *args: onSignal("int-signal"),
            on_str_signal=lambda *args: onSignal("str-signal"),
            on_bool_signal=lambda *args: onSignal("bool-signal"),
            on_boxed_signal=lambda *args: onSignal("boxed-signal"),
            on_complex_signal=lambda *args: onSignal("complex-signal"),
        )

        service.emit("int-signal", 42)
        service.emit("str-signal", "42")
        service.emit("bool-signal", True)
        service.emit("boxed-signal", object)
        service.emit("complex-signal", 42, "42", True, object)

        self.assertEqual(emittedSignals, expectedOutput)
        emittedSignals = []


if __name__ == "__main__":
    unittest.main()
