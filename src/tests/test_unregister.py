def test_unregister_success(client):
    email = "michael@mergington.edu"  # already signed up for Chess Club

    response = client.delete(f"/activities/Chess Club/signup?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Chess Club"

    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_student_not_signed_up_returns_404(client):
    response = client.delete("/activities/Chess Club/signup?email=notregistered@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_activity_not_found_returns_404(client):
    response = client.delete("/activities/Nonexistent Club/signup?email=someone@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
