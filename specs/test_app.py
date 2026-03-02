import pytest
from app import app  # Import your Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'DevOps Learner' in response.data

def test_submit_form(client):
    response = client.post('/submit', data={'name': 'Alice'})
    assert response.status_code == 200
    assert b'Thank you, Alice!' in response.data
