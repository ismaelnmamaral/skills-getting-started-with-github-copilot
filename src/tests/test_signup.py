def test_signup_success(client):
    email = "newstudent@mergington.edu"
    response = client.post(f"/activities/Chess Club/signup?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"

    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]


def test_signup_duplicate_returns_400(client):
    email = "michael@mergington.edu"  # already signed up for Chess Club

    response = client.post(f"/activities/Chess Club/signup?email={email}")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"


def test_signup_activity_not_found_returns_404(client):
    response = client.post("/activities/Nonexistent Club/signup?email=someone@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
