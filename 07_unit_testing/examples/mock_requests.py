

class MockResponse:
    def __init__(self, data, status_code):
        self.data = data
        self.status_code = status_code

    def json():
        return self.data


def mock_get_location():
    data = { ... }
    return MockResponse(data, 200)


def test_get_location(mocker):
    mocker.patch('requests.get', mock_get_location)
    # Somewhere in my test
    get_location()




def get_location():
    location = requests.get(...)
    data = location.json()

