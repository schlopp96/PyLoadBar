#!/usr/bin/env python3

from time import sleep as s

import tqdm

__version__ = '0.0.8'


class PyLoadBar:
    """Create simple loading sequences with ability to customize start/finish messages, toggle visual progress meter, and set time to completion."""

    def __init__(self):
        pass

    def load(self,
                 msg_loading: str = 'Loading',
                 msg_complete: str = 'Done!',
                 time: int = 5,
                 label: str = None,
                 enable_display: bool = True) -> None:
        """
        Start a loading sequence which includes start/completion messages, and an optional progress meter.

        - User may set custom start/completion messages using the parameters `msg_loading: str` and `msg_complete: str` respectively.
        - Set the sequence length in milliseconds using the `time: int` parameter.
            - Each unit of time = 0.1 seconds.
        - Display of the progress meter is activated by default, but may be disabled using the `enable_display` parameter.
        - The progress meter may be labeled using the `label: str` parameter (set to `None` by default).
            - Note that `enable_display` must be set to `True` for this to take effect.

        Examples:

            - Load sequence WITH progress meter (default):

                >>> bar_ON = PyLoadBar() # < Create class instance.
                >>> bar_ON.load(msg_loading='Printing', msg_complete='Complete!', time=50) # <- Will take 5 seconds to complete loading sequence.

            - Load sequence WITHOUT progress meter:

                >>> bar_OFF = PyLoadBar() # < Create class instance.
                >>> bar_OFF.load('Processing Information', 'Finished!', time=20, enable_display=False) # <- Will take 2 seconds to complete loading sequence.

        ---

        :param msg_loading: message to display during loading process, defaults to `"Loading"`.
        :type msg_loading: str, optional
        :param msg_complete: message to display upon load completion, defaults to `"Done!"`.
        :type msg_complete: str, optional
        :param time: time for loading sequence to complete measured in units of 0.1 seconds, defaults to `5`.
        :type time: int, optional
        :param label: label preceding progress bar, defaults to `None`.
        :type label: str, optional
        :param enable_display: toggle display of progress bar during loading process, defaults to `True`.
        :type enable_display: bool, optional
        :return: loading sequence.
        :rtype: None
        """

        match enable_display:
            case True:
                print(f'{msg_loading}...\n')
                for iter in tqdm.trange(time, desc=label):
                    s(0.1)
                    iter -= 1
                print(f'\n{msg_complete}')

            case False:
                print(f'{msg_loading}', end='')
                for iter in range(time):
                    print('.', end='')
                    s(0.1)
                    iter -= 1
                print(f'\n\n{msg_complete}')
        s(0.5) # Add a small delay to allow user to see completion message.