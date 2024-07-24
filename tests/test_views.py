import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_parse_address_success():
    client = APIClient()
    response = client.post(
        reverse("address-parse"),
        {"address": "123 Main St. Suite 100 Chicago, IL"},
        format="json",
    )
    assert response.status_code == 200
    assert response.data["status"] == "success"
    assert "AddressNumber" in response.data["parsed"]


@pytest.mark.django_db
def test_parse_address_failure():
    client = APIClient()
    response = client.post(
        reverse("address-parse"), {"address": "123 main st chicago il 123 main st"},
        format="json"
    )
    assert response.status_code == 400
    assert response.data["status"] == "error"
