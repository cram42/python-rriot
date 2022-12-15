"""Constants for testing."""


class RRIOTDataConstants(object):
    """Constants for testing RRIOTData."""

    BASIC_URL = "mock://basic.url"
    HAWK_URL = "mock://hawk.url"
    MQTT_URL = "mock://mqtt.url:1234"
    EMAIL = "mock.email@mock.url"
    EMAIL_INVALID_FORMAT = "mock.email#mock.url"
    USERNAME = "USERNAME123456"
    SECRET = "SECRET123456"
    HASH = "HASH123456"
    HOME_ID = 123456
    KEY = "KEY123456"


class BasicAPIConstants(object):
    """Constants for testing BasicAPI."""

    HOSTNAME = "basic.url"
    NEW_URL = f"mock://{HOSTNAME}"

    MOCK_EMAIL = "mock.email@mock.url"
    MOCK_EMAIL_FAIL = "mock.email#mock.url"
    MOCK_PASSWORD = "mock.password"
    MOCK_PASSWORD_FAIL = "mock.password.fail"
    MOCK_TOKEN = "token-data-in-base64-encoding"
    MOCK_TOKEN_FAIL = "invalid-token-value"

    RESPONSE_URL_EMAIL_INVALID = {
        "msg": "email format error",
        "data": None,
        "code": 2003,
    }

    RESPONSE_URL = {
        "code": 200,
        "msg": "success",
        "data": {
            "url": NEW_URL,
        },
    }

    RESPONSE_LOGIN = {
        "code": 200,
        "msg": "success",
        "data": {
            "uid": 1234567,
            "tokentype": "",
            "token": MOCK_TOKEN,
            "rruid": "rr0123456789abcdef",
            "region": "eu",
            "countrycode": "61",
            "country": "AU",
            "nickname": "nickname-value",
            "rriot": {
                "u": "rriot-username-value",
                "s": "rriot-secret-value",
                "h": "rriot-hash-value",
                "k": "rriot-key-value",
                "r": {
                    "r": "EU",
                    "a": "mock://hawk.url",
                    "m": "mock://mqtt.url:8883",
                    "l": "mock://unknown.url",
                },
                "tuyaDeviceState": 0,
                "avatarurl": "mock://avatar.url/avatar.png",
            },
        },
    }

    RESPONSE_LOGIN_FAIL = {
        "msg": "username or password error",
        "data": None,
        "code": 2012,
    }

    RESPONSE_HOMEDETAILS = {
        "code": 200,
        "msg": "success",
        "data": {
            "id": 1234567,
            "name": "home-name",
            "tuyaHomeId": 0,
            "rrHomeId": 7654321,
            "deviceListOrder": None,
        },
    }

    RESPONSE_INVALID_TOKEN = {
        "msg": "invalid token",
        "data": None,
        "code": 2010,
    }


class HawkAPIConstants(object):
    """Constants for testing HawkAPI."""

    _DATA = RRIOTDataConstants()

    URL = _DATA.HAWK_URL
    USERNAME = _DATA.USERNAME
    SECRET = _DATA.SECRET
    HASH = _DATA.HASH
    HOME_ID = _DATA.HOME_ID

    RESPONSE_HOMEDETAILS = {
        "api": "api-name-in-chinese",
        "result": {
            "id": _DATA.HOME_ID,
            "name": "home-name",
            "lon": None,
            "lat": None,
            "geoName": None,
            "products": [],
            "devices": [],
            "receivedDevices": [],
            "rooms": [],
        },
        "status": "ok",
        "success": True,
    }
