import unittest
from app import app

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Words and Paragraphs Counter', response.data)
        self.assertIn(b'COUNT', response.data)

    def test_count_route_valid_submission(self):
        data = {'text': 'This is a test text'}
        response = self.app.post('/count', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Words - 5 || Paragraphs - 1 || Characters - 19', response.data)

    def test_count_route_no_submission(self):
        response = self.app.post('/count')
        self.assertEqual(response.status_code, 400)

    def test_invalid_route(self):
        response = self.app.get('/invalid-route')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
