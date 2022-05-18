# PyLoadBar

> _**Minimalist load sequence/progress bar module.**_

---

## About

- Useful for small intermittant pauses between console text returns, or code actions.

- Customizable/optional loading and completion messages available to print to console (stdout).

  - Loading message defaults to `"Loading..."`.
  - Completion message defaults to `"Done!"`.

- Includes an _optional_ progress meter (simply change the `enable_display: bool` parameter to `False` if you wish to disable the progress meter), toggled on by default.

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

1. Download source code `.zip` archive from the PyLoadBar GitHub [releases](https://github.com/schlopp96/PyLoadBar/releases/latest) page and extract contents to desired location.

- OR:

1. Clone repository with the git client of your preference with:

   - `gh repo clone schlopp96/PyLoadBar`

2. Navigate to directory containing extracted contents, and open said folder within a terminal.

3. Enter `pip install -r requirements.txt` to install all dependencies for this package.

4. Finally, move the `"PyLoadBar-vx.x.x"` directory to your global Python 3rd-party package installation directory to be able to import `PyLoadBar` like any other module:

   - `"~Python/Lib/site-packages/HERE"`

5. Done!

---

## Usage

- Within a `.py` project, simply import the `PyLoadBar` module to start using your custom loading sequence.

- `PyLoadBar` is _very_ simple to use.

  - For example, try running the following:

```python
>>> from PyLoadBar import PyLoadBar

>>> bar = PyLoadBar() # Initialize a new `PyLoadBar` instance.

>>> def add50(x):
        bar.load(msg_loading='Adding 50 to x', msg_complete='Okay!', time=30, label='Solving', enable_display=True) # Call `load` method to start loading sequence.
        return x + 50

>>> print(add50(50))
```

- This will return:

```python
Adding 50 to x...

Solving: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5/5 [00:00<00:00,  8.94it/s].

Okay!

100
```

- The **_loading_** and **_loading complete_** messages can be customized by passing custom strings to the `msg_loading: str` and `msg_complete: str` parameters respectively.

- Note that the progress bar **can be toggled** using the `enable_display: bool` parameter.

- The time taken to complete the loading sequence can be determined using the `time: int` parameter.

  - Each unit of time is equivalent to 1/10th of a second.
  - Every 10 units = 1 second.
    - e.g. `load(time=5)` (default) would take 0.5 seconds to fill the progress bar.

- You may also label the progress bar with the `label: str` parameter (defaults to `None`).

- Example:

  ```python
  >>> from PyLoadBar import PyLoadBar

  >>> important_bar = PyLoadBar() # Initialize a new `PyLoadBar` instance.

  >>> important_bar.load('Important Stuff Happening', 'Day Saved!', 50, 'Saving Day') # Call `load` method to start loading sequence.

  Important Stuff Happening...

  Saving Day: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [00:05<00:00,  9.19it/s]

  Day Saved!
  ```

---

## Contributing to PyLoadBar

- If you wish to help contribute to this project, please run the following in your virtual env to acquire the necessary dependencies and tools you need to develop and run tests:

```python
pip install PyLoadBar[dev]
```

---

## Contact

- If you have any questions, comments, or concerns that cannot be addressed through the [project's GitHub repository](https://github.com/schlopp96/PyLoadBar), please feel free to contact me through my email address:

  - `schloppdaddy@gmail.com`

---
