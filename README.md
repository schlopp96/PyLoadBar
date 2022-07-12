# PyLoadBar

> _**Customizeable loading sequence/progress bar generator, enabling users to customize start/finish messages, toggle sequence type, and set total iterations among other features.**_

---

## About

- Useful for small intermittent pauses between console text returns, or visualizing the progress of a long-running process.

- Users can choose between two different loading sequences:

  - **A.** Progress-bar style loading sequence
  - **B.** Animated-text style loading sequence

- The desired loading sequence **can be toggled** using the `enable_bar: bool` parameter.

  - If `enable_bar: bool` is `False`, the progress-bar sequence will not be used, and the animated text-based loading sequence will be used instead.

- The text-based loading sequence displays the loading message followed by incrementing dots, all printed to the same line.

- Messages can be customized by passing custom strings to the `msg_loading: str` and `msg_complete: str` parameters respectively.

  - The loading message defaults to `"Loading..."`
  - The completion message defaults to `"Done!"`

- You may apply a label to the progress bar using the `label: str` parameter (defaults to `None`).

  - **NOTE:** `enable_bar: bool` must be set to `True` for a label to be assigned to the progress bar.

- The time taken to complete each iteration can be determined using the `min_iter: float` and `max_iter: float` parameters.
  - Each iteration length is randomized to a value between `min_iter: float` and `max_iter: float` seconds.
    - e.g. `start(min_iter=0.5, max_iter=1.5)` would take anywhere between 0.5 - 1.5 seconds to complete a single iteration.

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

    >>> important_bar = PyLoadBar(msg_loading='Important Stuff Happening', msg_complete='Day Saved!', label='Saving Day') # Initialize a new `PyLoadBar` instance.

    >>> important_bar.start(min_iter=0.05, max_iter=1.0, iter_total=10) # Call `start` method to begin loading sequence.

    Important Stuff Happening...

    Saving Day: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10

    Day Saved!
  ```

- Example of animated-text-based loading sequence:

  ```python
    >>> from PyLoadBar import PyLoadBar

    >>> bar = PyLoadBar(msg_loading='Loading', msg_complete='Done!', enable_bar=False) # Initialize loading sequence.

    >>> bar.start(iter_total=1) # Start animated-text loading sequence.

    # Note that during actual use case, text is printed to same line followed by incrementing dots:

    Loading
    Loading.
    Loading..
    Loading...

    Done!
  ```

---

## Contributing to PyLoadBar

- If you wish to help contribute to this project, please run the following in your virtual env to acquire the necessary dependencies and tools you need to develop and run tests:

  ```shell
    pip install PyLoadBar[dev]
  ```

---

## Contact

- If you have any questions, comments, or concerns that cannot be addressed through the [project's GitHub repository](https://github.com/schlopp96/PyLoadBar), please feel free to contact me through my email address:

  - `schloppdaddy@gmail.com`

---
