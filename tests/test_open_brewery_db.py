import pytest


@pytest.mark.parametrize("attrs", ["banjo", "pivot", "corner", "dog"])
def test_autocomplete(attrs, get_autocomplete):
    for fields in get_autocomplete(attrs).json():
        assert fields["id"] and fields["name"]
    assert get_autocomplete(attrs).status_code == 200
    print(get_autocomplete(attrs).json())


@pytest.mark.parametrize("attrs", ["banjo", "pivot", "corner", "dog"])
def test_autocomplete_status_code(attrs, get_autocomplete):
    assert get_autocomplete(attrs).status_code == 200


@pytest.mark.parametrize("attrs", sorted([
    "Cleveland",
    "Evergreen",
    "Oakland",
    "Bozeman",
    "Las Cruces",
    "Westminster",
    "Bangor"
    ]))
@pytest.mark.parametrize("key_str", ["dog"])
def test_search_breweries(attrs, key_str, get_search_breweries):
    test_city = {"city": attrs}
    assert test_city["city"] in get_search_breweries(key_str)


@pytest.mark.parametrize("name_brewery, id_brewery", [
    ("Banjo Brewing", "banjo-brewing-fayetteville"),
    ("Center Pivot", "center-pivot-quinter"),
    ("Corner Pub", "corner-pub-reedsburg"),
    ("Barrel Dog Brewing", "barrel-dog-brewing-evergreen")])
def test_single_brewery(name_brewery, id_brewery, get_single_brewery):
    assert name_brewery == get_single_brewery(id_brewery).json()["name"]


@pytest.mark.parametrize("id_brewery", [
    "banjo-brewing-fayetteville",
    "center-pivot-quinter",
    "corner-pub-reedsburg",
    "barrel-dog-brewing-evergreen"
    ])
def test_single_brewery_status_code(id_brewery, get_single_brewery):
    assert get_single_brewery(id_brewery).status_code == 200


@pytest.mark.parametrize("fields", [
    "id", "name",
    "street", "city",
    "phone", "state",
    "website_url", "country"])
def test_breweries(fields, get_breweries_list):
    for brewery in get_breweries_list.json():
        assert fields in brewery


def test_breweries_list(get_breweries_list):
    assert get_breweries_list.status_code == 200
