from PyLoadBar.main import PyLoadBar


def test_loadA():
    bar = PyLoadBar(time=1, enable_display=False)
    assert bar.load() is None


def test_loadB():
    bar = PyLoadBar("Taking sweet time",
                "Finally...\n\nTook long enough.")
    assert bar.load() is None


def test_loadC():
    bar = PyLoadBar('Exiting', 'Finished!!', enable_display=False)
    assert bar.load() is None


def test_loadD():
    bar = PyLoadBar(4, 3463463.4, time=3, enable_display=False)
    assert bar.load() is None
