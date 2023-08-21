import unittest
from flask_testing import TestCase

class FlaskAppTest(TestCase):

    def test_home_route(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertIn(b'Words and Paragraphs Counter', response.data)
        self.assertIn(b'COUNT', response.data)

    def test_count_route_valid_submission(self):
        data = {'text': 'This is a test text'}
        response = self.client.post('/count', data=data)
        self.assert200(response)
        self.assertIn(b'Words - 5 || Paragraphs - 1 || Characters - 19', response.data)

    def test_count_route_no_submission(self):
        response = self.client.post('/count')
        self.assert400(response)

    def test_invalid_route(self):
        response = self.client.get('/invalid-route')
        self.assert404(response)

if __name__ == '__main__':
    unittest.main()

