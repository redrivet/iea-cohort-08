from unittest.mock import patch
from funny import get_joke


def test_get_joke_success():
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'id': 12345,
            'joke': 'This is a test joke. Wakka wakka!',
            'status': 200
        }
        
        joke_id, joke = get_joke()
        assert joke_id == 12345
        assert joke == 'This is a test joke. Wakka wakka!'


def test_get_joke_server_error():
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 500
        mock_response.json.return_value = {}
        
        joke_id, joke = get_joke()
        assert joke_id is None
        assert joke == ''
