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

        - When instantiating a new :class:`PyLoadBar` object, you can set the following parameters:
            - Set custom start/completion messages by passing string to :param:`msg_loading` and :param:`msg_complete` respectively.
            - Toggle visual progress meter using :param:`enable_display`.
            - Apply label to progress meter by passing string to :param:`label` (set to `None` by default)
                    - Note that :param:`enable_display` must be set to `True` for this to take effect.

        - When calling :func:`start(self, iter_total, min_iter, max_iter)`:
            - Optionally set the total number of iterations to run using :param:`iter_total`, defaults to 5.
            - Optionally set the minimum/maximum iteration length in seconds using the :param:`min_iter` and :param:`max_iter` parameters respectively
                - Default values are `min_iter: 0.1` seconds and `max_iter: 1.0` seconds
    """

    def __init__(self,
                 msg_loading: str | None = 'Loading',
                 msg_complete: str | None = 'Done!',
                 label: str | None = None,
                 enable_display: bool = True) -> None:
        """Initialize loading sequence with set configuration.

        ---

        :param msg_loading: initial loading message, defaults to 'Loading'
        :type msg_loading: :class:`str` | None, optional
        :param msg_complete: final message displayed upon completion, defaults to 'Done!'
        :type msg_complete: :class:`str` | None, optional
        :param label: label displayed alongside progress bar, defaults to None
        :type label: :class:`str` | None, optional
        :param enable_display: toggle visible progress meter, defaults to `True`
        :type enable_display: :class:`bool`, optional
        :return: :class:`PyLoadBar` object
        :rtype: None
        """

        self.msg_loading: str | None = msg_loading
        self.msg_complete: str | None = msg_complete
        self.label: str | None = label
        self.enable_display: bool = enable_display

        if self.enable_display and self.msg_loading == 'Loading':
            self.msg_loading = f'{msg_loading}...'  # Add ellipses to default loading message.

    def start(
        self,
        iter_total: int = 5,
        min_iter: float = 0.05,
        max_iter: float = 1.0,
    ) -> None:
        """Start loading sequence.

        ---

        Settings:

            - Set the total number of iterations using the :param:`iter_total` parameter

            - Set the minimum/maximum iteration length in seconds using the :param:`min_iter` and :param:`max_iter` parameters respectively
                - Default values are `min_iter` = 0.1 seconds and `max_iter` = 1.0 seconds
                - Time of each iteration is randomized between values of :param:`min_iter` and :param:`max_iter`

        ---

        :param iter_total: total amount of iterations to run, defaults to 5
        :type iter_total: :class:`int`, optional
        :param min_iter: minimum possible time to complete an iteration, defaults to 0.05 seconds
        :type min_iter: :class:`int`, optional
        :param max_iter: maximum possible time to complete an iteration, defaults to 1.0 seconds
        :type max_iter: :class:`int`, optional
        :return: Loading sequence
        :rtype: None
        """

        try:
            if self.enable_display:
                self.__loadseq_A(iter_total, min_iter, max_iter)

            else:
                self.__loadseq_B(iter_total)

            sleep(
                0.5
            )  # Add small delay to allow user to read completion message.

        except Exception as e:
            print(f'Error: {e}')

    def __loadseq_A(self, iter_total: int, min_iter: float,
                    max_iter: float) -> None:
        """
        Run loading sequence and display current progress with graphical progress bar.

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

        print(f'\n{self.msg_loading}\n')

        # Start loading sequence.
        for iter in tqdm.trange(
                iter_total,
                desc=self.label,
                bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}]'):
            sleep(uniform(min_iter, max_iter))
            iter -= 1

        print(f'\n{self.msg_complete}\n')  # Print completion message.

    def __loadseq_B(self, iter_total: int) -> None:
        """Run loading sequence with animated text instead of graphical progress bar.

        ---

        Example:

        ```python
            >>> bar = PyLoadBar(msg_loading='Loading', msg_complete='Done!', enable_display=False) # Initialize loading sequence.
            >>> bar.start(iter_total=1) # Start loading sequence.
            >>> # Note that during actual use case, text is printed to same line with an animated dot sequence:

            > Loading > Loading. > Loading.. > Loading...

            Done!

        ```

        ---

        :param iter_total: Amount of iterations to run loading sequence
        :type iter_total: :class:`int`
        :return: loading sequence with animated text instead of progress bar.
        :rtype: None
        """

        for iter in range(iter_total):
            print(f'{self.msg_loading}', end='', flush=True)
            sleep(0.3)

            for _ in range(3):  # Animate dot sequence.
                print('.', end='')
                sleep(0.3)

            print('\x1b[2K\r', end='', flush=True)  # Clear line.

            iter -= 1  # Decrement iteration counter.

        print(f'\n{self.msg_complete}\n')  # Print completion message.
