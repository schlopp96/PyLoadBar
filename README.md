# PyLoad

> _**Simple, easy-to-use loading sequence module.**_

## About

---

- Useful for small intermittant pauses between console text returns, or code actions.

- Customizable, optional loading and completion messages available to print to the console.

  - Loading message defaults to `"Loading..."`.
  - Completion message defaults to `"Done!"`.

- Includes an _optional_ progress bar (simple change the `progressbar` parameter to equal `"True"`).

## Installing PyLoad

> _**`pip` installation coming soon...!**_

---

### Manual Installation

1. Download source code from the [PyLoad GitHub](https://github.com/PyLoad) repo.

2. Extract contents of the containing `**.zip` file to desired install location.

3. Navigate to directory containing extracted contents, and open said folder within a terminal.

4. Enter `pip install -r requirements.txt` to install all dependencies for this package.

5. Done!

---

## Usage

- Within a `.py` project, simply import the `PyLoad` module to start using your custom loading sequence.

- `PyLoad` is _very_ simple to use.

  - For example, try running the following:

        ```python

        from PyLoad import load

        equation = 20 * 20

        load(msg_loading = 'Solving', msg_complete = 'Okay!\n')

        print(equation)
        ```

  - This will return:

        ```
        Solving...

        100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5/5 [00:00<00:00,  8.94it/s].

        Okay!

        400
        ```

- Of course, the _loading_ and _loading complete_ messages can be customized by passing custom strings to the `msg_loading` and `msg_complete` parameters respectively.

- Note that the progress bar **can** be toggled using the `progressbar: bool` parameter within the `load(msg_complete: str, msg_loading: str, progressbar: bool, time: int)` method.

- The time taken to completely fill the progress bar can be determined using the `time: int` parameter.
  - Every 5 units = 1 second.
    - e.g. `load(time=10)` would take 2 seconds to fill the progress bar.

---

## Contact

- If you have any questions, comments, or concerns that cannot be alleviated through the [project's GitHub repository](https://github.com/schlopp96/PyLoad), please feel free to contact me through my email address:

  - `schloppdaddy@gmail.com`
