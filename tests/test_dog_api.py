import pytest


def test_by_breed_status(get_request_random_by_breed):
    assert get_request_random_by_breed.json()["status"] == "success"


def test_by_breed_have_jpg(get_request_random_by_breed):
    assert ".jpg" in get_request_random_by_breed.text.lower()


@pytest.mark.parametrize("attrs", [1, 2, 3, 4])
def test_random_multiple_have_jpg(attrs, get_request_random_multiple):
    assert ".jpg" in get_request_random_multiple(attrs).text.lower()


@pytest.mark.parametrize("attrs", [1, 2, 3, 4])
def test_random_multiple_status(attrs, get_request_random_multiple):
    assert get_request_random_multiple(attrs).json()["status"] == "success"


@pytest.mark.parametrize("sub_breeds", [
        "afghan",
        "basset",
        "blood",
        "english",
        "ibizan",
        "plott",
        "walker"
    ])
def test_list_all_sub_breeds(sub_breeds, get_request_list_all_sub_breeds):
    assert sub_breeds in get_request_list_all_sub_breeds
