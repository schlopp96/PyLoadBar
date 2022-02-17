#!/usr/bin/env python3

from logging import INFO
from logging import basicConfig as config
from logging import error, info
from os import chdir
from os.path import dirname, join
from time import sleep as s

import tqdm

#> Set CWD.
chdir(join(dirname(dirname(__file__))))

#< Logger configuration.
config(filename='./logs/logfile.log',
       format='%(asctime)s - %(levelname)s - %(message)s',
       level=INFO)


def load(
    msg_loading: str = 'Loading',
    msg_complete: str = 'Done!',
    progressbar: bool = True,
    time: int = 5,
) -> bool:
    """Breifly pause program while optionally displaying a customizable loading message, alongside an optional progress bar, to the console (stdout).

    - User may set custom strings through the parameters `msg_loading` and `msg_complete`.
    - Set the length of pause in seconds using the `time` parameter.
    - Displaying a progress bar is activated by default, but may be disables using the `progressbar` parameter.

    Parameters:
        :param msg_loading: message to display during loading process, defaults to `"Loading"`
        :type msg_loading: str, optional
        :param msg_complete: message to display upon load completion, defaults to `"Done!"`
        :type msg_complete: str, optional
        :param progressbar: whether to display progress bar during loading process, defaults to True
        :type progressbar: bool, optional
        :param time: time in seconds for progress bar to reach completion, defaults to `5` seconds.
        :type time: int, optional
        :return: loading sequence accompanied by an explanatory message to the user, and optional progress bar.
        :rtype: bool
    """

    try:
        #> Change loading message(s) to custom value(s):
        if msg_loading != 'Loading':
            msg_loading = str(msg_loading)
        if msg_complete != 'Done':
            msg_complete = str(msg_complete)

        #$ Return load sequence:
        if progressbar:
            info(
                f'Begin loading sequence using progress bar...\n"Loading" Message: "{msg_loading}"\n'
            )
            print(f'{msg_loading}...\n')
            for time in tqdm.trange(time):
                print('.', end='')
                s(0.1)
                time -= 1
        else:
            info(
                f'Begin loading sequence NOT using progress bar...\n"Loading" Message: "{msg_complete}"\n'
            )
            print(f'{msg_loading}', end='')
            for time in range(time):
                print('.', end='')
                s(0.1)
                time -= 1
        info(
            f'Completed loading process!\n"Completed" Message: "{msg_complete}"\n'
        )
        print(f'\n{msg_complete}')
        s(0.5)
        return True
    except ValueError as VE:
        error(f'{VE}')
        return False


if __name__ == '__main__':
    load()
