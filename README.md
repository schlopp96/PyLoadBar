# PyLoadBar

> _**Loading sequence/progress bar generator with options for users to customize start/finish messages, toggle between bar/text sequences, and set total iterations among other features.**_

---

## About

- Useful for small intermittent pauses between console text returns, or visualizing the progress of a long-running process.

- Users can choose between two different loading sequences:

  - **A.** _Progress-bar_ style loading sequence
  - **B.** _Animated-text_ style loading sequence

- When instantiating a `PyLoadBar` object, you may set the type of loading sequence using the `bar_sequence: bool` parameter.

- Once initialized, run the loading sequence using the `start()` method, and set sequence configuration using parameters.

- Messages can be customized by passing custom strings to the `msg_loading: str` and `msg_complete: str` parameters respectively.

  - The loading message defaults to `"Loading..."`
  - The completion message defaults to `"Done!"`

- You may apply a label to the progress bar using the `label: str` parameter (defaults to `None`).

  - **NOTE:** `bar_sequence: bool` must be set to `True` for a label to be assigned to the progress bar.

  - If `bar_sequence: bool` is `False`, the _progress-bar sequence_ will **not** be used, and the _animated text-based_ loading sequence **will** be used instead.

- When calling the `start()` method and using the _progress-bar_ sequence, the time taken to complete each iteration can be determined using the `min_iter: float` and `max_iter: float` parameters.

  - Each iteration length is randomized to a value between `min_iter: float` and `max_iter: float` seconds.
    - e.g. `start(min_iter=0.5, max_iter=1.5)` would take anywhere between 0.5 - 1.5 seconds to complete a single iteration.

- The _text-based_ loading sequence displays the loading message followed by incrementing dots, all printed to the same line.
  - Set number of seconds to complete a single text-sequence iteration using `txt_iter_speed: float`.
    - Defaults to `0.5` seconds per animation cycle.

---

## Installing PyLoadBar

### Using pip

> _Easiest_ method. Highly recommended over manual installation.

- Run the following to install:

  ```shell
  pip install PyLoadBar
  ```

- You should now be able to import `PyLoadBar` directly to your application.

---

### Manual Installation

> _Not_ recommended.

**1a.** Download the latest source code `.zip` archive from the PyLoadBar GitHub [releases](https://github.com/schlopp96/PyLoadBar/releases/latest) page and extract contents to the desired location.

- **OR:**

**1b.** Clone repository with the git client of your preference with:

```shell
gh repo clone schlopp96/PyLoadBar
```

**2.** Navigate to the directory containing extracted contents, and open said folder within a terminal.

**3.** Enter `pip install -r requirements.txt` to install all dependencies for this package.

**4.** Finally, move the `"PyLoadBar-Vx.x.x"` directory to your global Python 3rd-party package installation directory to be able to import `PyLoadBar` like any other module:

- `"~Python/Lib/site-packages/HERE"`

**5.** Done!

---

## Usage

- `PyLoadBar` is _very_ simple to use.

- Within a `.py` project, simply import the `PyLoadBar` module to start using your custom loading sequence.

- Example of standard loading sequence with `label` set to `'Solving'`:

  ```python
    >>> from PyLoadBar import PyLoadBar

    >>> important_bar = PyLoadBar() # Initialize a new `PyLoadBar` instance.

    >>> important_bar.start(msg_loading='Important Stuff Happening', msg_complete='Day Saved!', label='Saving Day', min_iter=0.05, max_iter=1.0, iter_total=10) # Call `start` method to begin loading sequence.

  ```

    ![alt](./assets/bar_sequence.gif)

- Example of animated-text-based loading sequence:

  ```python
    >>> from PyLoadBar import PyLoadBar

    >>> bar = PyLoadBar(bar_sequence=False) # Initialize loading sequence.

    >>> bar.start(msg_loading='Loading', msg_complete='Done!', iter_total=1, txt_iter_speed=1) # Start animated-text loading sequence.

  ```

    ![alt](./assets/text_sequence.gif)

---

## Contact

- If you have any questions, comments, or concerns that cannot be addressed through the [project's GitHub repository](https://github.com/schlopp96/PyLoadBar), please feel free to contact me through my email address:

  - `schloppdaddy@gmail.com`

---
