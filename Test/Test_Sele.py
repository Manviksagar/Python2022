import pytest


def test_m1():
    x = 2
    y = 3
    assert x == y, "Failed case"


def test_m2():
    x = 3
    y = 3
    assert x == y, "Pass case"


@pytest.mark.skip
def test_m3():
    x = 3
    y = 3
    assert x == y, "Pass case"


def test_sag(conffile):
    assert conffile == "chrome", "testpssed"


def test_conf(conf):
    print(conf)