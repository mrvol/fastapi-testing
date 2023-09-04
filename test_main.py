from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list) and 'Video' in result

def test_main_data_category_not_existing():
    response = client.get("/data/NOT-EXISTING")
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list) and len(result) == 0

def test_main_data_category_video():
    response = client.get("/data/Video")
    assert response.status_code == 200
    result = response.json()
    assert set(result[0].keys()) == {'api', 'desctription', 'link'}
    assert isinstance(result, list) and len(result) > 0

def test_main_data_category_video_and_search():
    response = client.get("/data/Video?search=NOT-EXISTING")
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list) and len(result) == 0
