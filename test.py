import pytest
from flask import Flask, render_template
import requests

# Create a Flask app for testing
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("your_template.html")

# Create a fixture for the Flask app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Define your tests
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Words and Paragraphs Counter' in response.data
    assert b'COUNT' in response.data

# Add more tests as needed

if __name__ == '__main__':
    pytest.main()


