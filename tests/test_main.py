from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_sch_get_home(mocker):
    mocker.patch(
        'app.lib.content.sch_content.get_home',
        return_value={'title': 'Search for benefits and services'}
    )
    response = client.get("/sch/home")
    assert response.status_code == 200
    assert response.json() == {'title': 'Search for benefits and services'}