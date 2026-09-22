def test_get_activities_returns_200(client):
    response = client.get("/activities")
    assert response.status_code == 200


def test_get_activities_contains_expected_activity(client):
    response = client.get("/activities")
    data = response.json()

    assert "Chess Club" in data
    chess_club = data["Chess Club"]
    assert set(["description", "schedule", "max_participants", "participants"]).issubset(chess_club.keys())
    assert "michael@mergington.edu" in chess_club["participants"]
