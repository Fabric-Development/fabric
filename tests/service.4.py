import unittest
from fabric.core import Service, Property, Builder


class TestService(Service):
    @Property(str, "read-write")
    def prop1(self):
        return self._prop1

    @prop1.setter
    def prop1(self, value: str):
        self._prop1 = value
        return

    @Property(str, "read-write")
    def prop2(self):
        return self._prop2

    @prop2.setter
    def prop2(self, value: str):
        self._prop2 = value
        return

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._prop1 = ""
        self._prop2 = ""


class TestServiceBuilder(unittest.TestCase):
    def testGetBuilder(self):
        service = TestService()
        builder = service.build()
        self.assertEqual(type(builder), Builder)

        self.assertIs(builder.set_prop1("4002").set_prop2("42").unwrap(), service)
        self.assertEqual(service.prop1, "4002")
        self.assertEqual(service.prop2, "42")

    def testGetBuilderCallback(self):
        service = TestService()
        builder = None

        def builder_callback(_, _builder: Builder):
            nonlocal builder
            builder = _builder
            return builder.set_prop1("4002").set_prop2("42").unwrap()

        self.assertIs(service.build(builder_callback), service)
        self.assertEqual(type(builder), Builder)
        self.assertEqual(service.prop1, "4002")
        self.assertEqual(service.prop2, "42")


if __name__ == "__main__":
    unittest.main()
