import pytest
from app import app  # Import your Flask app

@pytest.fixture
def client():
    # Setup a test client
    with app.test_client() as client:
        yield client

def test_home_page(client):
    # Test the home page route
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, DevOps!' in response.data

def test_submit_form(client):
    # Test the form submission route
    response = client.post('/submit', data={'name': 'Alice'})
    assert response.status_code == 200
    assert b'Thank you, Alice!' in response.data
