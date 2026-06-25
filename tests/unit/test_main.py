
def test_heathz_returns_version(client):
    response = client.get("/")
    assert b"<p>Hello NRAO!</p>" in response.data
