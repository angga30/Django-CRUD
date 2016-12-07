import os
import pytest

from .utils import assert_body_text

base_url = os.environ['BASE_URL']

@pytest.fixture
def selenium(selenium):
    selenium.maximize_window()
    return selenium


def test_search_expect_success(selenium):
    selenium.get(base_url)

    assert_body_text(
        selenium, 'BSM Web')

def test_search_expect_failure(selenium):
    selenium.get(base_url)

    assert_body_text(
        selenium, 'POOP')