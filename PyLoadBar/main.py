#!/usr/bin/env python3

import sys
from os.path import dirname
from random import uniform
from time import sleep

import tqdm

sys.path.insert(0, dirname(
    dirname(__file__)))  # Ensure module can be found by Python.

__version__ = '0.1.1'


class PyLoadBar:
    """Generate loading sequences with ability to customize start/finish messages, toggle visual progress meter, and set time to completion.

    ---

    Settings:

        - When instantiating a new :class:`PyLoadBar` object, you can set the sequence type using :param:`bar_sequence`.

        - When calling :func:`start(self, msg_loading, msg_complete, label, iter_total, min_iter, max_iter, txt_seq_speed)`:
            - Set custom start/completion messages by passing string to :param:`msg_loading` and :param:`msg_complete` respectively.
            - Optionally set the total number of iterations to run using :param:`iter_total`, defaults to 5.

            - If using bar-sequence:
                - Set the minimum/maximum iteration length in seconds using the :param:`min_iter` and :param:`max_iter` parameters respectively.
                    - Time taken by each individual iteration is randomized within range of :param:`min_iter` and :param:`max_iter`.
                - Apply label to progress meter by passing string to :param:`label` (set to `None` by default).

            - If using text-sequence:
                - Set number of seconds to complete a single text-sequence iteration using :param:`txt_seq_speed`.
                    - Defaults to `0.5` seconds per iteration/animation cycle.
    """

    def __init__(self, bar_sequence: bool = True) -> None:
        """Initialize loading sequence with set configuration.

        ---

        :param bar_sequence: toggle progress-bar loading sequence, defaults to `True`
        :type bar_sequence: :class:`bool`, optional
        :return: :class:`PyLoadBar` object
        :rtype: None
        """

        self.bar_sequence: bool = bar_sequence

    def start(
        self,
        msg_loading: str | None = 'Loading',
        msg_complete: str | None = 'Done!',
        label: str | None = None,
        iter_total: int = 5,
        min_iter: float = 0.01,
        max_iter: float = 0.5,
        txt_seq_speed: float = 0.5,
    ) -> None:
        """Start loading sequence.

        ---

        Settings:

            - Set custom start/completion messages by passing string to :param:`msg_loading` and :param:`msg_complete` respectively.
                - Note that :param:`bar_sequence` must be set to `True` for this to take effect.

            - Set the total number of iterations to complete using the :param:`iter_total`.
                - Defaults to 5 iterations.

            - If using bar-sequence:
                - Set the minimum/maximum iteration length in seconds using the :param:`min_iter` and :param:`max_iter` parameters respectively.
                    - Time taken by each individual iteration is randomized within range of :param:`min_iter` and :param:`max_iter`.
                        - :param:`min_iter` defaults to 0.01 seconds, :param:`max_iter` defaults to 0.5 seconds.
                - Apply label to progress meter by passing string to :param:`label` (set to `None` by default).

            - If using text-sequence:
                - Set number of seconds to complete a single text-sequence iteration using :param:`txt_seq_speed`.
                    - Defaults to `0.5` seconds per iteration/animation cycle.

        ---

        :param msg_loading: initial loading message, defaults to 'Loading'
        :type msg_loading: :class:`str` | None, optional
        :param msg_complete: final message displayed upon completion, defaults to 'Done!'
        :type msg_complete: :class:`str` | None, optional
        :param label: label displayed alongside progress bar, defaults to None
        :type label: :class:`str` | None, optional
        :param iter_total: total amount of iterations to run, defaults to 5
        :type iter_total: :class:`int`, optional
        :param min_iter: minimum possible time to complete an iteration, defaults to 0.01 seconds
        :type min_iter: :class:`float`, optional
        :param max_iter: maximum possible time to complete an iteration, defaults to 0.5 seconds
        :type max_iter: :class:`float`, optional
        :param txt_seq_speed: number of seconds to complete a single text-sequence iteration, defaults to 0.5 seconds
        :type txt_seq_speed: :class:`float`, optional
        :return: loading sequence
        :rtype: None
        """

        if self.bar_sequence and msg_loading == 'Loading':
            msg_loading = f'{msg_loading}...'  # Add ellipses to default progress-bar starting message.

        try:
            if self.bar_sequence:
                self.__bar_seq(msg_loading, msg_complete, label, iter_total,
                               min_iter, max_iter)

            else:
                self.__text_seq(msg_loading, msg_complete, iter_total,
                                txt_seq_speed)

            sleep(
                0.5
            )  # Add small delay to allow user to read completion message.

        except Exception as e:
            print(f'Error: {e}')

    @staticmethod
    def __bar_seq(msg_loading: str | None, msg_complete: str | None,
                  label: str | None, iter_total: int, min_iter: float,
                  max_iter: float) -> None:
        """
        Run loading sequence with progress bar.

        ---

        Example:

        ```python
            >>> bar = PyLoadBar() # Initialize loading sequence.
            >>> bar.start(msg_loading='Loading', msg_complete='Done!', label='Progress', iter_total=5, min_iter=0.1, max_iter=1.0) # Start loading sequence.

            Loading...

            Progress: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████▊| 5/5]

            Done!

        ```

        ---

        :param msg_loading: initial loading message
        :type msg_loading: :class:`str` | None
        :param msg_complete: final message displayed upon completion
        :type msg_complete: :class:`str` | None
        :param label: label displayed alongside progress bar
        :type label: :class:`str` | None
        :param iter_total: total amount of iterations to run
        :type iter_total: :class:`int`
        :param min_iter: minimum possible time (in seconds) an iteration can take
        :type min_iter: :class:`float`
        :param max_iter: maximum possible time (in seconds) an iteration can take
        :type max_iter: :class:`float`
        :return: Loading sequence with graphical progress bar.
        :rtype: None
        """

        print(f'{msg_loading}\n')

        # Start progress-bar iteration.
        for iter in tqdm.trange(
                iter_total,
                desc=label,
                bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}]'):
            sleep(uniform(min_iter, max_iter))
            iter -= 1

        print(f'\n{msg_complete}\n')  # Print completion message.

    @staticmethod
    def __text_seq(msg_loading: str | None, msg_complete: str | None,
                   iter_total: int, iter_speed: float) -> None:
        """Run text-based loading sequence.

        ---

        Example:

        ```python
            >>> bar = PyLoadBar(bar_sequence=False) # Initialize loading sequence.
            >>> bar.start(msg_loading='Loading', msg_complete='Done!', iter_total=1, txt_seq_speed=1) # Start loading sequence.
            >>> # Note that during actual use case, text is printed to same line followed by an animated '.' character sequence:

            # Would look like:
                It(1) line 1: \r"Loading"
                It(2) line 1: \r"Loading."
                It(3) line 1: \r"Loading.."
                It(4) line 1: \r"Loading..."

                Repeat(...)


                Line 3: "Done!"

        ```

        ---

        :param msg_loading: initial loading message
        :type msg_loading: :class:`str` | None
        :param iter_total: number of iterations to run during loading sequence
        :type iter_total: :class:`int`
        :param iter_speed: number of seconds to complete a single text-sequence iteration
        :type iter_speed: :class:`float`
        :return: animated text-based progress sequence
        :rtype: None
        """

        # Start text animation.
        for iter in range(iter_total):
            print(f'{msg_loading}', end='', flush=True)
            sleep(iter_speed / 4)

            for _ in range(3):  # Add 3 dots to `msg_loading` message.
                print('.', end='', flush=True)
                sleep(iter_speed / 4)

            print('\x1b[2K\r', end='', flush=True)  # Clear line.

            iter -= 1

        print(f'\n{msg_complete}\n')  # Print completion message.
