from PyLoadBar.main import PyLoadBar


def test_default_bar():
    seq = PyLoadBar()
    assert seq.start() is None


def test_default_text():
    seq = PyLoadBar(bar_sequence=False)
    assert seq.start() is None


def test_bar_params():
    seq = PyLoadBar()
    assert seq.start(msg_loading='STARTED TEST',
                     msg_complete='COMPLETE',
                     label="TESTING",
                     iter_total=25,
                     min_iter=0.001,
                     max_iter=0.25) is None


def test_text_params():
    seq = PyLoadBar(bar_sequence=False, )
    assert seq.start(msg_loading='TEST',
                     msg_complete='COMPLETE',
                     iter_total=5,
                     iter_speed=0.25) is None


def test_numbers_in_message_params():
    seq = PyLoadBar()
    assert seq.start(
        4, 3463463.4, label=123, iter_total=5, min_iter=0.001,
        max_iter=0.25) is None
