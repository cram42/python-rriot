"""Tests for RRIOTData class."""

from pytest import fixture
from rriot.rriot_data import RRIOTData

from .constants import RRIOTDataConstants as C

DATA_OBJECT = RRIOTData()
DATA_DICT: dict = {}


@fixture(name="_prepare_data")
def fixture_prepare_data():
    """Prepare data for tests."""
    DATA_OBJECT.basic_url = C.BASIC_URL
    DATA_OBJECT.hawk_url = C.HAWK_URL
    DATA_OBJECT.mqtt_url = C.MQTT_URL
    DATA_OBJECT.email = C.EMAIL
    DATA_OBJECT.username = C.USERNAME
    DATA_OBJECT.secret = C.SECRET
    DATA_OBJECT.hash = C.HASH
    DATA_OBJECT.home_id = C.HOME_ID
    DATA_OBJECT.key = C.KEY
    DATA_DICT["basic_url"] = C.BASIC_URL
    DATA_DICT["hawk_url"] = C.HAWK_URL
    DATA_DICT["mqtt_url"] = C.MQTT_URL
    DATA_DICT["email"] = C.EMAIL
    DATA_DICT["username"] = C.USERNAME
    DATA_DICT["secret"] = C.SECRET
    DATA_DICT["hash"] = C.HASH
    DATA_DICT["home_id"] = C.HOME_ID
    DATA_DICT["key"] = C.KEY


def test_create(_prepare_data):
    """Test creating an instance."""
    data = RRIOTData()
    assert isinstance(data, RRIOTData)


def test_to_dict(_prepare_data):
    """Test conversion to a dict."""
    data_dict = DATA_OBJECT.to_dict()
    assert isinstance(data_dict, dict)
    assert data_dict == DATA_DICT


def test_from_dict(_prepare_data):
    """Test conversion from a dict."""
    data = RRIOTData.from_dict(DATA_DICT)
    assert isinstance(data, RRIOTData)
    assert data.to_dict() == DATA_OBJECT.to_dict()
