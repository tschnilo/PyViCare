import unittest
from PyViCare.PyViCareService import ViCareDeviceAccessor, ViCareService
from PyViCare.PyViCareOAuthManager import AbstractViCareOAuthManager
from unittest.mock import Mock

class PyViCareServiceTest(unittest.TestCase):

    def setUp(self):
        self.oauth_mock = Mock()
        accessor = ViCareDeviceAccessor("[id]", "[serial]", "[device]")
        self.service = ViCareService(self.oauth_mock, accessor)
        
    def test_getProperty(self):
        self.service.getProperty("someprop")
        self.oauth_mock.get.assert_called_once_with('/equipment/installations/[id]/gateways/[serial]/devices/[device]/features/someprop')

    def test_setProperty_object(self):
        self.service.setProperty("someprop", "doaction", {'name': 'abc'})
        self.oauth_mock.post.assert_called_once_with('/equipment/installations/[id]/gateways/[serial]/devices/[device]/features/someprop/doaction', '{"name": "abc"}')

    def test_setProperty_string(self):
        self.service.setProperty("someprop", "doaction", '{}')
        self.oauth_mock.post.assert_called_once_with('/equipment/installations/[id]/gateways/[serial]/devices/[device]/features/someprop/doaction', '{}')
       