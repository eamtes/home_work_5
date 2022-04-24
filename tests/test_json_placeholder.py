import pytest


@pytest.mark.parametrize("key,value", [
    ("name", "John"),
    ("age", 25),
    ("city", "moscow"),
    ("phone", "samsung")
    ])
def test_post_json_placeholder(key, value, post_json_placeholder):
    assert key in post_json_placeholder(key, value).json()


@pytest.mark.parametrize("key,value", [
    ("name", "John"),
    ("age", 25),
    ("city", "moscow"),
    ("phone", "samsung")
    ])
def test_post_json_placeholder_status_code(key, value, post_json_placeholder):
    assert post_json_placeholder(key, value).status_code == 201


@pytest.mark.parametrize("id_value, attrs", [(1, 1), (6, 2), (11, 3)])
def test_json_placeholder_comments(id_value, attrs, get_json_placeholder_comments):
    assert get_json_placeholder_comments(attrs).json()[0]["id"] == id_value


@pytest.mark.parametrize("email, attrs", [
    ("Eliseo@gardner.biz", 1),
    ("Presley.Mueller@myrl.com", 2),
    ("Veronica_Goodwin@timmothy.net", 3)
    ])
def test_json_placeholder_comments(email, attrs, get_json_placeholder_comments):
    assert get_json_placeholder_comments(attrs).json()[0]["email"] == email


@pytest.mark.parametrize("id_value, attrs", [(1, 1), (6, 2), (11, 3)])
def test_json_placeholder_comments_status_code(id_value, attrs, get_json_placeholder_comments):
    assert get_json_placeholder_comments(attrs).status_code == 200
