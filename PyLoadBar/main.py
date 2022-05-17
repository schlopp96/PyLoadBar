#!/usr/bin/env python3

from time import sleep as s

import tqdm

__version__ = '0.0.8'


class PyLoadBar:
    """Breifly pause program while optionally displaying a customizable loading message, alongside an optional progress bar, to the console (stdout).

        - User may set custom loading/completion strings through the parameters `msg_loading` and `msg_complete`.
        - Set the length of pause in seconds using the `time` parameter.
            - Every increment of units = 0.1 seconds.
        - Displaying a progress bar is activated by default, but may be disabled using the `enable_display` parameter.
        - A custom label may be set using the `label` parameter.

        - Examples:
            - `>>> bar = PyLoadBar(time=5, label='Processing', enable_display=True)` <-- Will take 0.5 seconds to fill the progress bar.
            - `>>> bar = PyLoadBar(time=20, enable_display=False)` <-- Will take 2 seconds for `msg_complete` to display following `msg_loading`.

        ---

        :param msg_loading: message to display during loading process, defaults to `"Loading"`.
        :type msg_loading: str, optional
        :param msg_complete: message to display upon load completion, defaults to `"Done!"`.
        :type msg_complete: str, optional
        :param time: time for progress bar to reach completion in units of 0.1 seconds, defaults to `5`.
        :type time: int, optional
        :param label: label of progress bar, defaults to `None`.
        :type label: str, optional
        :param enable_display: whether to display progress bar during loading process, defaults to `True`
        :type enable_display: bool, optional
        :return: loading sequence accompanied by an explanatory message to the user, optionally visualized using a progress bar.
        :rtype: None
        """

    def __init__(self,
                 msg_loading: str = 'Loading',
                 msg_complete: str = 'Done!',
                 time: int = 5,
                 label: str = None,
                 enable_display: bool = True) -> None:

        self.msg_loading = msg_loading
        self.msg_complete = msg_complete
        self.time = time
        self.label = label
        self.enable_display = enable_display

    def load(self) -> None:
        if self.enable_display:
            print(f'{self.msg_loading}...\n')
            for time in tqdm.trange(self.time, desc=self.label):
                s(0.1)
                time -= 1
            print(f'\n{self.msg_complete}')
        else:
            print(f'{self.msg_loading}', end='')
            for time in range(self.time):
                print('.', end='')
                s(0.1)
                time -= 1
            print(f'\n\n{self.msg_complete}')
        s(0.5)