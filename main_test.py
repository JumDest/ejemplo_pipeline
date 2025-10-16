from main import get_weather
from unittest
from unittest.mock import patch


class Test(unittest, TestCase):
    @patch("main.request.get")
    def test_get_weather(mock_get):
        mock_get.return_value.json.return_value = {"temperature : 22"}
        result = get_weather()
        self.assertTrue (result, 22)

if__name__ == '__main__':
    unittest.main()