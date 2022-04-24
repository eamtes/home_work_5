def test_my_function(url, code, request_method):
    response = request_method(url)
    assert response.status_code == code
