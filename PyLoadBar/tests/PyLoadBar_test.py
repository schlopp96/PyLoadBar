from PyLoadBar.main import load


def test_loadA():
    assert load(time=1, enable_display=False) is None


def test_loadB():
    assert load("Taking sweet time",
                "Finally...\n\nTook long enough.") is None


def test_loadC():
    assert load("Exiting", "Finished!!", enable_display=False) is None


def test_loadD():
    assert load(4, 3463463.4, time=3, enable_display=False) is None
