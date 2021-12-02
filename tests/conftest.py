import pytest
from django.urls import reverse


@pytest.fixture
def url():
    # Get the path to the API
    return reverse('address-parse')
