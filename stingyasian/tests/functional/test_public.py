from stingyasian.tests import *

class TestPublicController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='public', action='index'))
        # Test response...
