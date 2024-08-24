import unittest
from fabric.core import Service


class TestServiceInit(unittest.TestCase):
    def testInitialize(self):
        service = Service()

    def testPropertiesCount(self):
        service = Service()
        message = "length of properties should be zero for pure Service objects"
        self.assertEqual(len(service.get_properties()), 0, message)

    def testSignalsCount(self):
        service = Service()
        message = "length of Signals should be zero for pure Service objects"
        self.assertEqual(len(service.get_signal_names()), 0, message)
        self.assertEqual(len(service.get_signal_ids()), 0, message)


if __name__ == "__main__":
    unittest.main()
