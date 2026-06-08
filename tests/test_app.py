import requests, time

BASE = "http://localhost:5000"

def test_index_returns_200():
    r = requests.get(f"{BASE}/")
    assert r.status_code == 200

def test_index_has_message():
    r = requests.get(f"{BASE}/")
    data = r.json()
    assert "message" in data
    assert "Flask" in data["message"]

def test_health_db_connected():
    r = requests.get(f"{BASE}/health")
    assert r.status_code == 200
    assert r.json()["db"] == "connected"

def test_data_endpoint():
    r = requests.get(f"{BASE}/data")
    assert r.status_code == 200
    assert "server_time" in r.json()
