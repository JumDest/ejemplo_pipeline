import unittest
import json
from main import app

class FlaskApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_suma(self):
        response = self.app.get('/suma?a=5&b=10')
        data = json.loads(response.get_data())
        self.assertEqual(data['result'], 15)

    def test_multiplicar(self):
        response = self.app.post('/multiplicar', json={'a': 5, 'b': 10})
        data = json.loads(response.get_data())
        self.assertEqual(data['result'], 50)

if __name__ == '__main__':
    unittest.main()