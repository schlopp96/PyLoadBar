#!/usr/bin/env python3
#%==============================================================================================%#

import logging
from os import chdir
from os.path import dirname
from time import sleep as s

import tqdm

#> Set CWD:
chdir(dirname(__file__))

__version__ = '0.0.8'

#< Set Log Configuration:
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s - %(levelname)s] : %(message)s')
fh = logging.FileHandler('./logs/logfile.log')
fh.setFormatter(formatter)
logger.addHandler(fh)

#%==============================================================================================%#


def load(msg_loading: str = 'Loading',
         msg_complete: str = 'Done!',
         time: int = 5,
         label: str = None,
         enable_display: bool = True) -> None:
    """Breifly pause program while optionally displaying a customizable loading message, alongside an optional progress bar, to the console (stdout).

    - User may set custom loading/completion strings through the parameters `msg_loading` and `msg_complete`.
    - Set the length of pause in seconds using the `time` parameter.
        - Every increment of units = 0.1 seconds.
    - Displaying a progress bar is activated by default, but may be disabled using the `enable_display` parameter.
    -
    - Examples:
        - `>>> load(time=5, enable_display=True)` will take around 0.5 seconds to fill the progress bar.
        - `>>> load(time=20, enable_display=False)` will take around 2 seconds for `msg_complete` to display, following `msg_loading`.

    Parameters:
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

    try:
        #> Change loading message(s) to custom value(s):
        if msg_loading != 'Loading':
            msg_loading = msg_loading
        if msg_complete != 'Done':
            msg_complete = msg_complete

        #$ Return load sequence:
        if enable_display:
            return loadseq_enabled(msg_loading, msg_complete, time, label)
        else:
            return loadseq_disabled(msg_loading, msg_complete, time)
    except ValueError as ve:
        logger.exception(f'{ve}')


def loadseq_disabled(msg_loading, msg_complete, time: int = 5) -> None:
    logger.info(
        f'Begin loading sequence NOT using progress bar...\n-> Loading Message: "{msg_loading}"\n'
    )
    print(f'{msg_loading}', end='')
    for time in range(time):
        print('.', end='')
        s(0.1)
        time -= 1
    logger.info(
        f'Completed loading process!\n-> Completed Message: "{msg_complete}"\n-> Time to completion: {(time * 0.1)+0.2} seconds.\n'
    )
    print(f'\n\n{msg_complete}')
    s(0.5)


def loadseq_enabled(msg_loading,
                    msg_complete,
                    time: int = 5,
                    label: str = None) -> None:
    logger.info(
        f'Begin loading sequence using progress bar...\n-> Loading Message: "{msg_loading}"\n'
    )
    print(f'{msg_loading}...\n')
    for time in tqdm.trange(time, desc=label):
        s(0.1)
        time -= 1
    logger.info(
        f'Completed loading process!\n-> Completed Message: "{msg_complete}"\n-> Time to completion: {(time * 0.1)+0.2} seconds.\n'
    )
    print(f'\n{msg_complete}')
    s(0.5)


if __name__ == '__main__':
    load()
