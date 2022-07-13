from ..main import PyLoadBar


def test_seqA():
    seq = PyLoadBar()
    assert seq.start() is None


def test_seqB():
    seq = PyLoadBar(bar_sequence=False)
    assert seq.start() is None


def test_seqC():
    seq = PyLoadBar()
    assert seq.start(msg_loading='TEST',
                    msg_complete='COMPLETE',
                    label="LOADING", iter_total=25, min_iter=0.001, max_iter=0.25) is None


def test_seqD():
    seq = PyLoadBar(bar_sequence=False,
                    )
    assert seq.start(msg_loading='TEST',
                     msg_complete='COMPLETE',
                     iter_total=5,
                     txt_seq_speed=0.25) is None


def test_seqE():
    seq = PyLoadBar()
    assert seq.start(
        4, 3463463.4, label=123, iter_total=5, min_iter=0.001,
        max_iter=0.25) is None
