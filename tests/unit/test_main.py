
def test_heathz_returns_version(client):
    response = client.get("/")
    assert b"<p>Hello World!</p>" in response.data
