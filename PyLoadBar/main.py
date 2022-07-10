#!/usr/bin/env python3

import sys
from os import chdir
from os.path import dirname
from random import uniform
from time import sleep

import tqdm

sys.path.insert(0, dirname(
    dirname(__file__)))  # Ensure module can be found by Python.

chdir(dirname(__file__))  # Change working directory to main module.

__version__ = '0.0.9'


class PyLoadBar:
    """Generate loading sequences with ability to customize start/finish messages, toggle visual progress meter, and set time to completion.

    ---

    Settings:

        - Set custom start/completion messages by passing string to `msg_loading` and `msg_complete` respectively.

        - Toggle visual progress meter using `enable_display`.

        - Apply label to progress meter by passing string to `label: str | None` (set to `None` by default)
                - Note that `enable_display: bool` must be set to `True` for this to take effect.

        - When calling :func:`start`:

            - Optionally set the total number of iterations to run using `iter_total: int`

            - Optionally set the minimum/maximum iteration length in seconds using the `min_iter: float` and `max_iter: float` parameters respectively
                - Default values are `min_iter: 0.1` seconds and `max_iter: 1.0` seconds

    """

    def __init__(self,
                 msg_loading: str | None = 'Loading...',
                 msg_complete: str | None = 'Done!',
                 label: str | None = None,
                 enable_display: bool = True):
        """Initialize loading sequence with set configuration.

        ---

        :param msg_loading: initial loading message string, defaults to 'Loading...'
        :type msg_loading: :class:`str` | None, optional
        :param msg_complete: final message string displayed upon completion, defaults to 'Done!'
        :type msg_complete: :class:`str` | None, optional
        :param label: label displayed alongside progress bar, defaults to None
        :type label: :class:`str` | None, optional
        :param enable_display: toggle visible progress meter, defaults to True
        :type enable_display: :class:`bool`, optional
        """

        self.msg_loading: str | None = msg_loading
        self.msg_complete: str | None = msg_complete
        self.label: str | None = label
        self.enable_display: bool = enable_display

    def start(
        self,
        iter_total: int = 5,
        min_iter: float = 0.1,
        max_iter: float = 1.0,
    ) -> None:
        """Start loading sequence.

        ---

        - Set the total number of iterations using the `iter_total: int` parameter

        - Set the minimum/maximum iteration length in seconds using the `min_iter: float` and `max_iter: float` parameters respectively
            - Default values are `min_iter: 0.1` seconds and `max_iter: 1.0` seconds

        ---

        :param iter_total: number of iter_total until completion, defaults to 5
        :type iter_total: :class:`int`, optional
        :param min_iter: minimum possible time to complete an iteration, defaults to 1
        :type min_iter: :class:`int`, optional
        :param max_iter: maximum possible time to complete an iteration, defaults to 5
        :type max_iter: :class:`int`, optional
        """

        if self.enable_display:
            return self.__loadseq_A(iter_total, min_iter, max_iter)

        else:
            return self.__loadseq_B(iter_total)

    def __loadseq_A(self, iter_total: int, min_iter: float,
                    max_iter: float) -> None:
        """
        Run loading sequence and display progress with graphical progress bar.

        :param iter_total: total number of iter_total to run
        :type iter_total: :class:`int`
        :param min_iter: minimum possible time (in seconds) an iteration can take
        :type min_iter: :class:`float`
        :param max_iter: maximum possible time (in seconds) an iteration can take
        :type max_iter: :class:`float`
        """

        print(f'\n{self.msg_loading}\n')

        for iter in tqdm.trange(iter_total, desc=self.label):
            sleep(uniform(min_iter, max_iter))
            iter -= 1

        print(f'\n{self.msg_complete}\n')

        # Add a small delay to allow user to see completion message.
        sleep(0.5)

    def __loadseq_B(self, iter_total: int) -> None:
        """
        Run non-graphical loading sequence.

        :param iter_total: Amount of iter_total to run loading sequence
        :type iter_total: :class:`int`
        :return: nonvisual loading sequence

        """

        print(f'\n{self.msg_loading}', end='')

        for iter in range(iter_total):
            for _ in range(3):
                print('.', end='')
                sleep(0.3)
            print('\b\b\b', end='')
            iter -= 1

        print(f'\n\n{self.msg_complete}\n')

        # Add a small delay to allow user to see completion message.
        sleep(0.5)
