import pytest


@pytest.fixture
def conffile():
    driver = "chrome"
    return driver


@pytest.fixture
def conf():
    return "Sagar conffile"
