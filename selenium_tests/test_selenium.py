import os
import pytest
from urlparse import urljoin
from .utils import assert_body_text

base_url = os.environ['BASE_URL']


@pytest.fixture
def selenium(selenium):
    selenium.maximize_window()
    return selenium


def test_base(selenium):
    selenium.get(base_url)

    assert_body_text(
        selenium, 'BSM Web', 'Data', 'Case Numbers', 'Diagnoses',
        'Projects', 'Samples', 'Sequencing Centers',
        "This is a Proof of Concept Data Management app for the Brain "
        "Somatic Mosaicism project and its collaborators.")


def test_search_expect_results(selenium):
    selenium.get(urljoin(base_url, "sequencingcenter/create"))

    # Create a Sequencing Center
    seq_center_name = "Test Sequencing Center"
    selenium.find_element_by_id('id_name').send_keys(seq_center_name)
    selenium.find_element_by_xpath('//input[@type="submit"]').click()

    selenium.get(base_url)

    search_term = "Sequencing"
    selenium.find_element_by_id('search_input').send_keys(search_term)

    assert_body_text(
        selenium,
        "SequencingCenter: {}".format(seq_center_name),
        "Showing 1 to 1 of 1 entries",
    )

def test_search_expect_no_results(selenium):
    selenium.get(base_url)

    search_term = "Coffee is tasty"
    selenium.find_element_by_id('search_input').send_keys(search_term)

    assert_body_text(selenium, 'No results found for: {}'.format(search_term))
