#!/usr/bin/env python3

from datetime import datetime
from logging import INFO
from logging import basicConfig
from logging import error, info
from os import chdir, mkdir
from os.path import dirname, exists
from time import sleep as s

import tqdm

#> Set CWD.
chdir(dirname(__file__))


def createLogs():
    try:
        if exists(r'./logs/logsfile.log') == False:
            mkdir(r'./logs')
            fh = open(r'./logs/logfile.log', 'x')
            fh.close()
            info('Log file created.')
    except FileExistsError:
        info('Log file opened.')


createLogs()


def log_header() -> int:
    """Generate log header including time and date of logger startup/shutdown.

    :return: formatted log header.
    :rtype: int
    """
    with open(r'./logs/logfile.log', 'a') as logfile:
        return logfile.write(
            f'Date: {datetime.now().strftime("%Y-%m-%d")}\nTime: {datetime.now().strftime("%H:%M:%S")}\n{"=".ljust((16),"=")}\n\n'
        )


def log_footer() -> int:
    """Generate log footer including date and time of logger startup/shutdown.

    :return: formatted log footer,
    :rtype: int
    """
    with open(r'./logs/logfile.log', 'a') as logfile:
        return logfile.write(
            f'End of log file for date: {datetime.now().strftime("%Y-%m-%d")}\nTime: {datetime.now().strftime("%H:%M:%S")}\n{"=".ljust((16),"=")}\n\n'
        )


def load(
    msg_loading: str = 'Loading',
    msg_complete: str = 'Done!',
    progressbar: bool = True,
    time: int = 5,
) -> bool:
    """Breifly pause program while optionally displaying a customizable loading message, alongside an optional progress bar, to the console (stdout).

    - User may set custom strings through the parameters `msg_loading` and `msg_complete`.
    - Set the length of pause in seconds using the `time` parameter.
        - Every increment of 5 units = 5 seconds.
    - Displaying a progress bar is activated by default, but may be disables using the `progressbar` parameter.
    - Examples:
        - `>>> load(time=10, progressbar=True)` will take 2 seconds to fill the progress bar.
        - `>>> load(time=10, progressbar=False)` will take 2 seconds for `msg_complete` to display, following `msg_loading`.

    Parameters:
        :param msg_loading: message to display during loading process, defaults to `"Loading"`
        :type msg_loading: str, optional
        :param msg_complete: message to display upon load completion, defaults to `"Done!"`
        :type msg_complete: str, optional
        :param progressbar: whether to display progress bar during loading process, defaults to `True`
        :type progressbar: bool, optional
        :param time: time in seconds for progress bar to reach completion, defaults to `5`.
        :type time: int, optional
        :return: loading sequence accompanied by an explanatory message to the user, and optional progress bar.
        :rtype: bool
    """

    try:
        #> Change loading message(s) to custom value(s):
        if msg_loading != 'Loading':
            msg_loading = msg_loading
        if msg_complete != 'Done':
            msg_complete = msg_complete

        #$ Return load sequence:
        if progressbar:
            info(
                f'Begin loading sequence using progress bar...\n"Loading" Message: "{msg_loading}"\n'
            )
            print(f'{msg_loading}...\n')
            for time in tqdm.trange(time):
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
    #< Logger configuration.
    createLogs()
    basicConfig(filename='./logs/logfile.log',
                filemode='a',
                format='%(asctime)s - %(levelname)s - %(message)s',
                level=INFO)
    log_header()
    load()
    log_footer()
