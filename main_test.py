from main import get_weather
from unittest
from unittest.mock import patch


class Test(unittest, TestCase):
    @patch("main.request.get")
    def test_get_weather(mock_get):
        mock_get.return_value.json.return_value = {"temperature : 22"}
        result = get_weather()
        self.assertTrue (result, 22)
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if__name__ == '__main__':
    unittest.main()