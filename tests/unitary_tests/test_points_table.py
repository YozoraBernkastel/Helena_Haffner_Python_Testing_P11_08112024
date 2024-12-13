from tests.mock import POINTS_TABLE_PAGE

def test_points_table_route(client, mock_clubs, mock_competitions):
    response = client.get("/points_table")
    assert response.status_code == 200
    assert POINTS_TABLE_PAGE in response.data

