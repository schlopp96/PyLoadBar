from ..main import PyLoadBar


def test_seqA():
    seq = PyLoadBar()
    assert seq.start() is None


def test_seqB():
    seq = PyLoadBar(enable_bar=False)
    assert seq.start() is None


def test_seqC():
    seq = PyLoadBar(msg_loading='TEST',
                    msg_complete='COMPLETE',
                    label="LOADING")
    assert seq.start(iter_total=25, min_iter=0.001, max_iter=0.25) is None


def test_seqD():
    seq = PyLoadBar(enable_bar=False,
                    msg_loading='TEST',
                    msg_complete='COMPLETE')
    assert seq.start(iter_total=5, txt_seq_speed=0.25) is None


def test_seqE():
    seq = PyLoadBar(4, 3463463.4, label=123)
    assert seq.start(iter_total=5, min_iter=0.001, max_iter=0.25) is None
