from fishbase.fish_http_status import *


class TestHttpStatus(object):

    def setup_method(self):
        self.BAD_HTTP_STATUS = -1

    def teardown_method(self):
        self.BAD_HTTP_STATUS = None

    def test_status_informational(self):
        assert is_informational(HTTP_CONTINUE) is True
        assert is_informational(self.BAD_HTTP_STATUS) is False

    def test_status_success(self):
        assert is_success(HTTP_OK) is True
        assert is_success(self.BAD_HTTP_STATUS) is False

    def test_status_redirection(self):
        assert is_redirection(HTTP_MULTIPLE_CHOICES) is True
        assert is_redirection(self.BAD_HTTP_STATUS) is False

    def test_status_client_error(self):
        assert is_client_error(HTTP_BAD_REQUEST) is True
        assert is_client_error(self.BAD_HTTP_STATUS) is False

    def test_status_server_error(self):
        assert is_server_error(HTTP_INTERNAL_SERVER_ERROR) is True
        assert is_server_error(self.BAD_HTTP_STATUS) is False
