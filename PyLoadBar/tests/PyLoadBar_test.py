from ..main import PyLoadBar



def test_loadA():
    bar = PyLoadBar()
    assert bar.start() is None


def test_loadB():
    bar = PyLoadBar("Taking sweet time",
                    "Finally...\n\nTook long enough.", enable_display=False)
    assert bar.start(iter_total=3) is None


def test_loadC():
    bar = PyLoadBar('Exiting', 'Finished!!')
    assert bar.start() is None


def test_loadD():
    bar = PyLoadBar(
        4,
        3463463.4)
    assert bar.start(min_iter=0.3, max_iter=0.05) is None
