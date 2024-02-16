import unittest
from api import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_numbers(self):
        response = self.app.get('/plus/2/3')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('result', data)
        self.assertEqual(data['result'], 5)

    def test_add_numbers_negative(self):
        response = self.app.get('/plus/-2/3')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('result', data)
        self.assertEqual(data['result'], 1)

if __name__ == '__main__':
    unittest.main()