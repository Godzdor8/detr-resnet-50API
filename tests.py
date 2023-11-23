import pytest
from main import app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    client = TestClient(app)
    yield client


def test_persons(client):
    response = client.get(
        "/get-objects-by-image",
        params={
            "url": "https://img.freepik.com/premium-photo/set-of-casual-people-on-white_394555-1982.jpg",
        }
    )
    assert response.status_code == 200
    assert response.json() == ["Detected person with confidence 0.998 at location [245.76, 26.18, 282.6, 173.25]",
                               "Detected person with confidence 0.997 at location [561.84, 25.38, 609.63, 174.48]",
                               "Detected person with confidence 0.998 at location [8.32, 23.82, 55.1, 172.98]",
                               "Detected person with confidence 0.998 at location [162.1, 8.61, 208.57, 174.88]",
                               "Detected person with confidence 0.997 at location [83.33, 20.52, 136.05, 173.4]",
                               "Detected person with confidence 0.998 at location [316.01, 16.93, 367.71, 173.56]",
                               "Detected person with confidence 0.998 at location [478.15, 10.13, 515.91, 173.61]",
                               "Detected person with confidence 0.998 at location [400.14, 26.71, 444.43, 177.16]"]


def test_cars(client):
    response = client.get(
        "/get-objects-by-image",
        params={
            "url": "https://img.freepik.com/premium-vector/set-of-colored-cars_152789-12.jpg?w=2000",
        }
    )
    assert response.status_code == 200
    assert response.json() == ["Detected car with confidence 0.999 at location [1113.26, 1469.76, 1780.43, 1743.88]",
                               "Detected car with confidence 0.965 at location [167.38, 1369.46, 960.4, 1753.94]",
                               "Detected car with confidence 0.996 at location [1098.33, 253.83, 1802.7, 520.32]",
                               "Detected car with confidence 0.997 at location [224.32, 261.87, 914.84, 519.56]",
                               "Detected car with confidence 0.998 at location [219.59, 824.46, 914.25, 1098.42]",
                               "Detected truck with confidence 0.945 at location [1076.62, 779.28, 1841.59, 1090.57]"]


def test_invalid_query(client):
    response = client.get(
        "/get-objects-by-image",
        params={
            "url": "abcdefg",
        }
    )
    assert response.status_code == 200
    assert response.json() == {"url": "This is not url"}
