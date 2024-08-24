import unittest
from typing import Any
from fabric.core import Service, Property


class BaseService(Service):
    int_prop = Property(int)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.int_prop = 42


class TestServiceProperties(unittest.TestCase):
    class InheritedService(BaseService):
        str_prop = Property(str)

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.str_prop = "42"

    class ServiceWithProperties(Service):
        int_prop = Property(int)
        str_prop = Property(str)
        bool_prop = Property(bool, default_value=False)
        boxed_prop = Property(object)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.int_prop = 42
            self.str_prop = "42"
            self.bool_prop = True
            self.boxed_prop = object
            self._decor_prop: str = "decor-prop"

        @Property(str)
        def decor_prop(self):
            return self._decor_prop

        @decor_prop.setter
        def decor_prop(self, value):
            self._decor_prop = value
            return

    def testOrphaned(self):
        int_prop = Property(int)
        str_prop = Property(str)
        bool_prop = Property(bool, default_value=False)
        boxed_prop = Property(object)

        int_prop = Any
        str_prop = Any
        bool_prop = Any
        boxed_prop = Any

        for prop in [int_prop, str_prop, bool_prop, boxed_prop]:
            self.assertEqual(prop, Any)

    def testOrphanedDifferentTypes(self):
        int_prop = Property(int)
        str_prop = Property(str)
        bool_prop = Property(bool, default_value=False)
        boxed_prop = Property(object)

        int_prop = 42
        str_prop = "42"
        bool_prop = True
        boxed_prop = object

        self.assertEqual(int_prop, 42)
        self.assertEqual(str_prop, "42")
        self.assertEqual(bool_prop, True)
        self.assertEqual(boxed_prop, object)

    def testServicePropertiesSimple(self):
        service = self.ServiceWithProperties()
        self.assertEqual(service.int_prop, 42)
        self.assertEqual(service.str_prop, "42")
        self.assertEqual(service.bool_prop, True)
        self.assertEqual(service.boxed_prop, object)

    def testServicePropertiesComplex(self):
        service = self.ServiceWithProperties()
        self.assertEqual(service.int_prop, 42)
        self.assertEqual(service.str_prop, "42")
        self.assertEqual(service.bool_prop, True)
        self.assertEqual(service.boxed_prop, object)

        service["int-prop"] = 4002
        self.assertEqual(service.int_prop, 4002)
        service["str-prop"] = "4002"
        self.assertEqual(service.str_prop, "4002")
        service["bool-prop"] = False
        self.assertEqual(service.bool_prop, False)
        service["boxed-prop"] = None
        self.assertEqual(service.boxed_prop, None)

        self.assertEqual(service["int-prop"], 4002)
        self.assertEqual(service["str-prop"], "4002")
        self.assertEqual(service["bool-prop"], False)
        self.assertEqual(service["boxed-prop"], None)

    def testPropertyNotify(self):
        notifiedSignals: list[str] = []
        expectedOutput = [
            "int-prop",
            "str-prop",
            "bool-prop",
            "boxed-prop",
            "decor-prop",
        ]

        def onNotify(propertyName: str):
            notifiedSignals.append(propertyName)

        service = self.ServiceWithProperties(
            notify_int_prop=lambda *args: onNotify("int-prop"),
            notify_str_prop=lambda *args: onNotify("str-prop"),
            notify_bool_prop=lambda *args: onNotify("bool-prop"),
            notify_boxed_prop=lambda *args: onNotify("boxed-prop"),
            notify_decor_prop=lambda *args: onNotify("decor-prop"),
        )
        service.notify("decor-prop")  # decorated properties doesn't get initialized
        self.assertEqual(notifiedSignals, expectedOutput)
        notifiedSignals.clear()

        service["int-prop"] = 4002
        service["str-prop"] = "4002"
        service["bool-prop"] = False
        service["boxed-prop"] = None
        service["decor-prop"] = "decor"
        self.assertEqual(notifiedSignals, expectedOutput)

    def testPropertyNotifyAndCheckValue(self):
        notifiedSignals: dict[str, Any] = {}
        expectedOutput = {
            "int-prop": 42,
            "str-prop": "42",
            "bool-prop": True,
            "boxed-prop": object,
            "decor-prop": "decor-prop",
        }
        expectedModifiedOutput = {
            "int-prop": 4002,
            "str-prop": "4002",
            "bool-prop": False,
            "boxed-prop": None,
            "decor-prop": "decor",
        }

        def onNotify(self: Service, propertyName: str):
            notifiedSignals[propertyName] = self[propertyName]

        service = self.ServiceWithProperties(
            notify_int_prop=lambda self, *args: onNotify(self, "int-prop"),
            notify_str_prop=lambda self, *args: onNotify(self, "str-prop"),
            notify_bool_prop=lambda self, *args: onNotify(self, "bool-prop"),
            notify_boxed_prop=lambda self, *args: onNotify(self, "boxed-prop"),
            notify_decor_prop=lambda self, *args: onNotify(self, "decor-prop"),
        )
        service.notify("decor-prop")
        self.assertEqual(notifiedSignals, expectedOutput)
        notifiedSignals.clear()

        service["int-prop"] = 4002
        service["str-prop"] = "4002"
        service["bool-prop"] = False
        service["boxed-prop"] = None
        service["decor-prop"] = "decor"
        self.assertEqual(notifiedSignals, expectedModifiedOutput)
        notifiedSignals.clear()
        del service

        service = self.ServiceWithProperties()

        for propertyName, _ in expectedOutput.items():
            service.connect(
                f"notify::{propertyName}",
                lambda self, *args, pName=propertyName: onNotify(self, pName),
            )

        service["int-prop"] = 4002
        service["str-prop"] = "4002"
        service["bool-prop"] = False
        service["boxed-prop"] = None
        service["decor-prop"] = "decor"
        self.assertEqual(notifiedSignals, expectedModifiedOutput)

    def testInheritedProperties(self):
        service = self.InheritedService()
        self.assertEqual(service.int_prop, 42)
        self.assertEqual(service.str_prop, "42")

        service.int_prop = 4002
        service.str_prop = "4002"
        self.assertEqual(service.int_prop, 4002)
        self.assertEqual(service.str_prop, "4002")


if __name__ == "__main__":
    unittest.main()
