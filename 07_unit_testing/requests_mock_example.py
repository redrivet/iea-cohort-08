
class MockResponse:
    '''Class to fake out the actual Response class that requests returns.
       Supports a json() function that returns a dictionary, and a status code
       (so you can test for error statuses more easily)'''
    def __init__(self, json_data, status_code):
        '''Accepts a dict of data to mimic the API response, and a status code
        value'''
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        '''Just returns whatever was passed in in __init__'''
        return self.json_data


def mock_get_location(*args, **kwargs):
    '''This function is what will replace requests.get during testing
       We can ignore the arguments since we're not actually making
       a web request.  We'll just pretend we're making one and return a
       static dictionary as if it were the response.'''
   response_json = { }  # Put data in here to pretend to mimic the API
   return MockResponse(response_json, 200)



# Inside one of your tests
def test_get_location(mocker):
    # This replaces the "requests.get" function with the supplied function
    # dynamically, just for the span of this test
    # Now, whenever our actual code under test calls "requests.get" it will
    # call our mock function instead, and return our MockResponse object
    mocker.patch('requests.get', mock_get_location)

    # Function under test
    data = get_location()
