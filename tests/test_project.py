def test_homepage(client, mock_clubs, mock_competitions):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data


def test_connexion_with_existing_mail(client, mock_clubs, mock_competitions):
    response = client.post("/showSummary", data={"email": "test@test.test"})
    assert response.status_code == 200
    assert b"<title>Summary | GUDLFT Registration</title>" in response.data


def test_connexion_with_unknown_mail(client, mock_clubs, mock_competitions):
    response = client.post("/showSummary", data={"email": "test2@test.test"})
    assert response.status_code == 200
    assert not b"<title>Summary | GUDLFT Registration</title>" in response.data
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data

