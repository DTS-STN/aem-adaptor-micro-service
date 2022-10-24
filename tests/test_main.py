import unittest

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@unittest.skip("Cache is returned in test")
def test_read_sch_get_home(mocker):
    mocker.patch(
        "app.lib.content.sch_content.get_home", return_value={"title": "Test title"}
    )
    response = client.get("/sch/home")
    assert response.status_code == 200
    assert response.json() == {"title": "Test title"}
