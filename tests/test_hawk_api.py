"""Tests for HawkAPI class."""

import pytest

from rriot.hawk_api import HawkAPI
from rriot.constants import HawkAPIConstants as HC

from .constants import HawkAPIConstants as C


def simulate_response(request, _context):
    """Simulate basic API responses."""
    base_url = f"{request.scheme}://{request.hostname}"

    if base_url == str.lower(C.URL):
        if request.path_url == HC.PATH_HOMEDETAILS.format(home_id=C.HOME_ID):
            return C.RESPONSE_HOMEDETAILS
        return

    return None


@pytest.fixture(name="_prepare")
def fixture_prepare(requests_mock):
    """Prepare for tests."""
    requests_mock.get(
        C.URL + HC.PATH_HOMEDETAILS.format(home_id=C.HOME_ID),
        json=simulate_response,
    )


def test_create():
    """Test creating an instance."""
    api = HawkAPI()
    assert isinstance(api, HawkAPI)


def test_get(_prepare):
    """Test get()."""
    api = HawkAPI()
    api.setup(C.URL, C.USERNAME, C.SECRET, C.HASH, C.HOME_ID)
    home_details = api.get(HC.PATH_HOMEDETAILS)
    assert isinstance(home_details, dict)
