from PyLoadBar.main import PyLoadBar


def test_loadA():
    bar = PyLoadBar()
    assert bar.load(time=1, enable_display=False) is None


def test_loadB():
    bar = PyLoadBar()
    assert bar.load("Taking sweet time",
                    "Finally...\n\nTook long enough.") is None


def test_loadC():
    bar = PyLoadBar()
    assert bar.load('Exiting', 'Finished!!', enable_display=False) is None


def test_loadD():
    bar = PyLoadBar()
    assert bar.load(4, 3463463.4, time=3, enable_display=False) is None
