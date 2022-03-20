# PyLoadBar

> _**Simple, easy-to-use loading sequence module.**_

---

## About

- Useful for small intermittant pauses between console text returns, or code actions.

- Customizable, optional loading and completion messages available to print to the console.

  - Loading message defaults to `"Loading..."`.
  - Completion message defaults to `"Done!"`.

- Includes an _optional_ progress bar (simply change the `enable_display: bool` parameter to equal `False` if you wish to disable the progress bar), toggled on by default.

---

## Installing PyLoadBar

### Using pip

> _Easiest_ method. Highly recommended over manual installation.

- Run the following to install:

```python
    pip install PyLoadBar
```

- You should now be able to import `PyLoadBar` directly to your application.

---

### Manual Installation

> _Not_ recommended.

1. Download source code from the [PyLoadBar GitHub repo](https://github.com/schlopp96/PyLoadBar).

2. Extract contents of the containing `**.zip` file to desired install location.

3. Navigate to directory containing extracted contents, and open said folder within a terminal.

4. Enter `pip install -r requirements.txt` to install all dependencies for this package.

5. Finally, move the `"PyLoadBar-vx.x.x"` diretory to your global Python 3rd-party package installation directory to be able to import `PyLoadBar` like any other module:

   - `"path/to/python/Lib/site-packages/here"`

6. Done!

---

## Usage

- Within a `.py` project, simply import the `PyLoadBar` module to start using your custom loading sequence.

- `PyLoadBar` is _very_ simple to use.

  - For example, try running the following:

```python
from PyLoadBar import load

def add50(x):
  load(f'Adding 50 to {x}', 'Okay!\n')
  return x + 50

print(add50(50))
```

- This will return:

```python
Solving...

100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5/5 [00:00<00:00,  8.94it/s].

Okay!

100
```

- Of course, the _loading_ and _loading complete_ messages can be customized by passing custom strings to the `msg_loading: str` and `msg_complete: str` parameters respectively.

- Note that the progress bar **can be toggled** using the `enable_display: bool` parameter within the `load(msg_complete: str, msg_loading: str, time: int, enable_display: bool)` method.

- The time taken to completely fill the progress bar can be determined using the `time: int` parameter.

  - Every 10 units = 1 second.
    - e.g. `load(time=5)` (default) would take 0.5 seconds to fill the progress bar.

- You may also label the progress bar with the `label: str` parameter, defaults to `None`.

- Example:

  ```python
  >>> from PyLoadBar import load

  >>> load('Important Stuff Happening', 'Day Saved!', 50, 'Saving Day')
  Important Stuff Happening...

  Saving Day: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [00:05<00:00,  9.19it/s]

  Day Saved!
  ```

---

## Contributing to PyLoadBar

- If you wish to help contribute to this project, along with the tools you need to develop and run tests, please run the following in your virtual env:

```python
pip install PyLoadBar[dev]
```

---

## Contact

- If you have any questions, comments, or concerns that cannot be addressed through the [project's GitHub repository](https://github.com/schlopp96/PyLoadBar), please feel free to contact me through my email address:

  - `schloppdaddy@gmail.com`

---
