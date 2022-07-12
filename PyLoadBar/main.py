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

__version__ = '0.0.9.1'


class PyLoadBar:
    """Generate loading sequences with ability to customize start/finish messages, toggle visual progress meter, and set time to completion.

    ---

    Settings:

        - When instantiating a new :class:`PyLoadBar` object, you can set the following parameters:
            - Set custom start/completion messages by passing string to :param:`msg_loading` and :param:`msg_complete` respectively.
            - Toggle visual progress meter using :param:`enable_bar`.
            - Apply label to progress meter by passing string to :param:`label` (set to `None` by default)
                    - Note that :param:`enable_bar` must be set to `True` for this to take effect.

        - When calling :func:`start(self, iter_total, min_iter, max_iter, txt_seq_speed)`:
            - Optionally set the total number of iterations to run using :param:`iter_total`, defaults to 5.
            - Optionally set the minimum/maximum iteration length in seconds using the :param:`min_iter` and :param:`max_iter` parameters respectively
                - Default values are `min_iter: 0.1` seconds and `max_iter: 1.0` seconds
    """

    def __init__(self,
                 msg_loading: str | None = 'Loading',
                 msg_complete: str | None = 'Done!',
                 label: str | None = None,
                 enable_bar: bool = True) -> None:
        """Initialize loading sequence with set configuration.

        ---

        :param msg_loading: initial loading message, defaults to 'Loading'
        :type msg_loading: :class:`str` | None, optional
        :param msg_complete: final message displayed upon completion, defaults to 'Done!'
        :type msg_complete: :class:`str` | None, optional
        :param label: label displayed alongside progress bar, defaults to None
        :type label: :class:`str` | None, optional
        :param enable_bar: toggle visible progress bar, defaults to `True`
        :type enable_bar: :class:`bool`, optional
        :return: :class:`PyLoadBar` object
        :rtype: None
        """

        self.msg_loading: str | None = msg_loading
        self.msg_complete: str | None = msg_complete
        self.label: str | None = label
        self.enable_bar: bool = enable_bar

        if self.enable_bar and self.msg_loading == 'Loading':
            self.msg_loading = f'{msg_loading}...'  # Add ellipses to default progress-bar starting message.

    def start(
        self,
        iter_total: int = 10,
        min_iter: float = 0.01,
        max_iter: float = 0.5,
        txt_seq_speed: float = 0.5,
    ) -> None:
        """Start loading sequence.

        ---

        Settings:

            - Set the total number of iterations to complete using the :param:`iter_total` parameter.

            - Set the minimum/maximum iteration length in seconds using the :param:`min_iter` and :param:`max_iter` parameters respectively.
                - Time taken by each individual iteration is randomized within range of :param:`min_iter` and :param:`max_iter`.

            - Set number of seconds to complete a single text-sequence iteration using :param:`txt_seq_speed`.
                -

        ---

        :param iter_total: total amount of iterations to run, defaults to 5
        :type iter_total: :class:`int`, optional
        :param min_iter: minimum possible time to complete an iteration, defaults to 0.05 seconds
        :type min_iter: :class:`float`, optional
        :param max_iter: maximum possible time to complete an iteration, defaults to 0.25 seconds
        :type max_iter: :class:`float`, optional
        :param txt_seq_speed: number of seconds to complete a single text-sequence iteration, defaults to 0.5 seconds
        :type txt_seq_speed: :class:`float`, optional
        :return: enable loading sequence
        :rtype: None
        """

        try:
            if self.enable_bar:
                self.__bar_seq(iter_total, min_iter, max_iter)

            else:
                self.__text_seq(iter_total, txt_seq_speed)

            sleep(
                0.5
            )  # Add small delay to allow user to read completion message.

        except Exception as e:
            print(f'Error: {e}')

    def __bar_seq(self, iter_total: int, min_iter: float,
                  max_iter: float) -> None:
        """
        Run loading sequence with progress bar.

        ---

        Example:

        ```python
            >>> bar = PyLoadBar(msg_loading='Loading', msg_complete='Done!', label='Progress') # Initialize loading sequence.
            >>> bar.start(iter_total=5, min_iter=0.1, max_iter=1.0) # Start loading sequence.

            Loading...

            Progress: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████▊| 5/5]

            Done!

        ```

        ---

        :param iter_total: total amount of iterations to run
        :type iter_total: :class:`int`
        :param min_iter: minimum possible time (in seconds) an iteration can take
        :type min_iter: :class:`float`
        :param max_iter: maximum possible time (in seconds) an iteration can take
        :type max_iter: :class:`float`
        :return: Loading sequence with graphical progress bar.
        :rtype: None
        """

        print(f'{self.msg_loading}\n')

        # Start progress-bar iteration.
        for iter in tqdm.trange(
                iter_total,
                desc=self.label,
                bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}]'):
            sleep(uniform(min_iter, max_iter))
            iter -= 1

        print(f'{self.msg_complete}\n')  # Print completion message.

    def __text_seq(self, iter_total: int, iter_speed: float) -> None:
        """Run text-based loading sequence.

        ---

        Example:

        ```python
            >>> bar = PyLoadBar(msg_loading='Loading', msg_complete='Done!', enable_bar=False) # Initialize loading sequence.
            >>> bar.start(iter_total=1) # Start loading sequence.
            >>> # Note that during actual use case, text is printed to same line followed by an animated '.' character sequence:

            # Would look like:
                It(1) line 1: \r`bar.msg_loading`
                It(2) line 1: \r`bar.msg_loading`.
                It(3) line 1: \r`bar.msg_loading`..
                It(4) line 1: \r`bar.msg_loading`...

                Repeat(...)


                Line 3: `bar.msg_complete`

        ```

        ---

        :param iter_total: Amount of iterations to run loading sequence
        :type iter_total: :class:`int`
        :param iter_speed: Seconds per text-sequence iteration
        :type iter_speed: :class:`float`
        :return: animated text-based progress sequence
        :rtype: None
        """

        # Start text animation.
        for iter in range(iter_total):
            print(f'{self.msg_loading}', end='', flush=True)
            sleep(iter_speed / 4)

            for _ in range(3):  # Add 3 dots to `msg_loading` message.
                print('.', end='', flush=True)
                sleep(iter_speed / 4)

            print('\x1b[2K\r', end='', flush=True)  # Clear line.

            iter -= 1

        print(f'\n{self.msg_complete}\n')  # Print completion message.
