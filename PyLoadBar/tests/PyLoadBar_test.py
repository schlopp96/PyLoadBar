from PyLoadBar.load import load


def test_loadA():
    assert load(time=3, progressbar=False) is None


def test_loadB():
    assert load("Taking sweet time",
                "Fucking finally...\n\nJesus christ.") is None


def test_loadC():
    assert load("Exiting", "Finished!!", progressbar=False) is None


def test_loadD():
    assert load(4, 3463463.4, 3, False) is None
