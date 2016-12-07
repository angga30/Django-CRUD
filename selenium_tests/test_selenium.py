import os
from urlparse import urljoin

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


def test_create_object(selenium):
    selenium.get(urljoin(base_url, "sequencingcenter/create"))

    # Create a Sequencing Center
    seq_center_name = "Test Sequencing Center"
    selenium.find_element_by_id('id_name').send_keys(seq_center_name)
    selenium.find_element_by_xpath('//input[@type="submit"]').click()

    assert_body_text(
        selenium,
        "SequencingCenter: {}".format(seq_center_name),
    )
