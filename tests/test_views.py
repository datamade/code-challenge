import ast


def test_api_parse_succeeds(client, mocker):
    # Arrange
    address_string = '123 main st chicago il'
    prepared_string = address_string.replace(" ", "+")
    url = "/api/parse/?address=" + prepared_string

    # Mock a healthy usaddress response.
    # We mock because we don't need to test the usaddress library.
    # We can trust that usaddress has tests of its own.
    mock_address_components = {
      "AddressNumber": "123",
      "StreetName": "main",
      "StreetNamePostType": "st",
      "PlaceName": "chicago",
      "StateName": "il",
    }
    mock_address_type = "Street Address"
    mock_return = [mock_address_components, mock_address_type]
    mocker.patch('usaddress.tag', return_value=mock_return)

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    content = ast.literal_eval(response.content.decode('utf-8'))
    assert content.get('input_string') == address_string
    assert content.get('address_type') == mock_address_type
    assert content.get('address_components') == mock_address_components


def test_api_parse_raises_error_if_usaddress_raises_error(client, mocker):
    # Arrange
    address_string = '123 main st chicago il 123 main st'
    prepared_string = address_string.replace(" ", "+")
    url = "/api/parse/?address=" + prepared_string

    # Mock an Exception within usaddress.
    # We mock because we don't need to test the usaddress library.
    # We can trust that usaddress has tests of its own.
    exception_message = 'mocked error'
    mocker.patch('usaddress.tag', side_effect=Exception(exception_message))

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 400
    content = ast.literal_eval(response.content.decode('utf-8'))
    assert content.get("detail") == exception_message


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
