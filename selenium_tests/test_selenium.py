import os
import pytest
from .utils import assert_body_text

base_url = os.environ['BASE_URL']


@pytest.fixture
def selenium(selenium):
    selenium.maximize_window()
    return selenium


def test_base(selenium):
    selenium.get(base_url)

    assert_body_text(
        selenium, 'BSM Web', 'Data',
        "This is a Proof of Concept Data Management app for the Brain "
        "Somatic Mosaicism project and its collaborators.")
