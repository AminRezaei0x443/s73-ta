import json


def test_join(test_app):
    response = test_app.post("/network/join", data=json.dumps({
        "capacity": 1
    }))
    assert response.status_code == 200
    j = response.json()
    assert j["id"] >= 0