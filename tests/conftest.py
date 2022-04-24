import argparse

import pytest
import requests


# ----------------------------------------------------------------------------------------------
# -------Для тестирование Dog_API---------------------------------------------------------------

@pytest.fixture
def get_request_random_by_breed():
    return requests.get("https://dog.ceo/api/breed/hound/images/random")


@pytest.fixture
def get_request_random_multiple():

    def _request(attr):
        return requests.get(f"https://dog.ceo/api/breed/hound/images/random/{attr}")

    return _request


@pytest.fixture
def get_request_list_all_sub_breeds():
    return requests.get("https://dog.ceo/api/breed/hound/list").json()["message"]

# ----------------------------------------------------------------------------------------------
# -------Для тестирование Open_Brewery_DB-------------------------------------------------------

@pytest.fixture
def get_autocomplete():

    def _request(attr):
        return requests.get(f"https://api.openbrewerydb.org/breweries/autocomplete?query={attr}")

    return _request

@pytest.fixture
def get_search_breweries():

    def _request(attr):
        response = requests.get(f"https://api.openbrewerydb.org/breweries/search?query={attr}")
        list_brewery_city = []
        for t in response.json():
            list_brewery_city.append(t["city"])
        return list_brewery_city

    return _request

@pytest.fixture
def get_single_brewery():

    def _request(attr):
        return requests.get(f"https://api.openbrewerydb.org/breweries/{attr}")

    return _request

@pytest.fixture
def get_breweries_list():
    return requests.get("https://api.openbrewerydb.org/breweries")

# ----------------------------------------------------------------------------------------------
# -------Для тестирование {JSON} Placeholder----------------------------------------------------

@pytest.fixture
def post_json_placeholder():

    def _request(name, attr):
        return requests.post("https://jsonplaceholder.typicode.com/posts", json={name: attr})

    return _request

@pytest.fixture
def get_json_placeholder_comments():

    def _request(attr):
        return requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={attr}")

    return _request

# ----------------------------------------------------------------------------------------------
# -------Для тестирование тестовой функции на 2 параметра---------------------------------------

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru"
    )

    parser.addoption(
        "--code",
        default=200,
        type=int
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"]
    )

@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def code(request):
    return request.config.getoption("--code")

@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))

# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
