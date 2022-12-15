"""Tests for BasicAPI class."""

import urllib
import pytest

from rriot.basic_api import BasicAPI
from rriot.constants import BasicAPIConstants as BC
from rriot.exceptions import (
    InvalidCredentialsException,
    InvalidEmailFormatException,
    InvalidTokenException,
)
from rriot.rriot_data import RRIOTData

from .constants import BasicAPIConstants as C

TEST_EMAIL = "test.email@mailserver.url"
TEST_USERNAME_INVALID_FORMAT = "test-username"
TEST_USERNAME_INVALID = TEST_EMAIL
TEST_PASSWORD_INVALID = "test-password"


def simulate_response(request, context):
    """Simulate basic API responses."""
    base_url = f"{request.scheme}://{request.hostname}"

    if base_url == str.lower(BC.DEFAULT_URL):
        if request.path_url == BC.PATH_URL:
            form_data = urllib.parse.parse_qs(request.text)
            email = form_data.get("email")[0]
            if email == C.MOCK_EMAIL:
                return C.RESPONSE_URL
            elif email == C.MOCK_EMAIL_FAIL:
                return C.RESPONSE_URL_EMAIL_INVALID

    elif base_url == str.lower(C.NEW_URL):

        if request.path_url == BC.PATH_LOGIN:
            form_data = urllib.parse.parse_qs(request.text)
            username = form_data.get("username")[0]
            password = form_data.get("password")[0]
            if (username == C.MOCK_EMAIL) and (password == C.MOCK_PASSWORD):
                return C.RESPONSE_LOGIN
            else:
                return C.RESPONSE_LOGIN_FAIL

        elif request.path_url == BC.PATH_HOMEDETAILS:
            if request.headers["Authorization"] == C.MOCK_TOKEN:
                return C.RESPONSE_HOMEDETAILS
            else:
                return C.RESPONSE_INVALID_TOKEN

    return None


@pytest.fixture(name="_prepare")
def fixture_prepare(requests_mock):
    """Prepare for tests."""
    requests_mock.post(BC.DEFAULT_URL + BC.PATH_URL, json=simulate_response)
    requests_mock.post(C.NEW_URL + BC.PATH_LOGIN, json=simulate_response)
    requests_mock.get(C.NEW_URL + BC.PATH_HOMEDETAILS, json=simulate_response)


def test_create():
    """Test creating an instance."""
    api = BasicAPI()
    assert isinstance(api, BasicAPI)


def test_login_invalidemailformat(_prepare):
    """Test login() with an invalid format email."""
    api = BasicAPI()
    with pytest.raises(Exception) as exc_info:
        api.login(C.MOCK_EMAIL_FAIL, C.MOCK_PASSWORD)
    assert exc_info.type is InvalidEmailFormatException


def test_login_invalidcredentials(_prepare):
    """Test login() with invalid credentials."""
    api = BasicAPI()
    with pytest.raises(Exception) as exc_info:
        api.login(C.MOCK_EMAIL, C.MOCK_PASSWORD_FAIL)
    assert exc_info.type is InvalidCredentialsException


def test_login(_prepare):
    """Test login() with an "valid" credentials."""
    api = BasicAPI()
    rriot_data = api.login(C.MOCK_EMAIL, C.MOCK_PASSWORD)
    assert isinstance(rriot_data, RRIOTData)


def test_get(_prepare):
    """Test get()."""
    api = BasicAPI()
    api.set_parameters(
        url=C.NEW_URL,
        token=C.MOCK_TOKEN,
    )
    home_details = api.get(BC.PATH_HOMEDETAILS)
    assert isinstance(home_details, dict)


def test_get_invalidtoken(_prepare):
    """Test get() with an invalid token."""
    api = BasicAPI()
    api.set_parameters(
        url=C.NEW_URL,
        token=C.MOCK_TOKEN_FAIL,
    )
    with pytest.raises(Exception) as exc_info:
        api.get(BC.PATH_HOMEDETAILS)
    assert exc_info.type is InvalidTokenException
