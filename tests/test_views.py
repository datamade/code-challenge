import ast


def test_api_parse_succeeds(client):
    # Arrange
    address_string = '123 main st chicago il'
    prepared_string = address_string.replace(" ", "+")
    url = "/api/parse/?address=" + prepared_string

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    content = ast.literal_eval(response.content.decode('utf-8'))
    assert content.get('input_string') == address_string
    assert content.get('address_type') == "Street Address"
    address_components = content.get('address_components')
    assert address_components.get('AddressNumber') == "123"
    assert address_components.get('StreetName') == "main"
    assert address_components.get('StreetNamePostType') == "st"
    assert address_components.get('PlaceName') == "chicago"
    assert address_components.get('StateName') == "il"


def test_api_parse_raises_error_for_repeated_label(client):
    # Arrange
    address_string = '123 main st chicago il 123 main st'
    prepared_string = address_string.replace(" ", "+")
    url = "/api/parse/?address=" + prepared_string

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 400
    content = ast.literal_eval(response.content.decode('utf-8'))
    err = "Unable to tag this string because more than one area of the string has the"
    assert err in content.get("detail")


def test_api_parse_raises_error_if_blank_address(client):
    # Arrange
    url = "/api/parse/?address="

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 400
    content = ast.literal_eval(response.content.decode('utf-8'))
    assert content.get("detail") == "Non-blank address query param must be provided."


def test_api_parse_raises_error_if_no_address(client):
    # Arrange
    url = "/api/parse/"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 400
    content = ast.literal_eval(response.content.decode('utf-8'))
    assert content.get("detail") == "Non-blank address query param must be provided."
