# US States Game

A geography guessing game built with Python's `turtle` graphics library. A blank map of the
United States is displayed, and you guess state names one at a time — each correct guess is
written onto the map at the right spot.

## Demo

<!-- Add a screenshot or GIF of the game here -->

## How it works

- `blank_states_img.gif` is registered as a custom turtle shape and drawn as the background.
- `50_states.csv` stores each state name along with the `x`/`y` turtle coordinates where its
  label should be written.
- Guesses are read through `Screen.textinput`, which keeps the game in a single window instead of
  using the terminal.
- The score in the window title updates as you go, and already-guessed states can't be guessed
  twice.
- Typing `Exit` closes the window and writes the states you missed to `states_not_guessed.csv`.

## Requirements

- Python 3.6+
- [pandas](https://pandas.pydata.org/)
- `turtle` (bundled with Python — see the note below)

## Running the game

```bash
pip install pandas
python main.py
```

Make sure your terminal is using Python 3:

```bash
python3 main.py   # macOS / Linux
py main.py        # Windows
```

> **Note on turtle:** The `turtle` module relies on Tkinter, which is included with most Python
> installs but not always (e.g. some Linux distributions split it into a separate package). If you
> get `ModuleNotFoundError: No module named 'tkinter'`, install it via your package manager
> (`sudo apt install python3-tk`) or from the official Python installer.

## Files

| File | Description |
| --- | --- |
| `main.py` | The whole game. |
| `50_states.csv` | State names and their map coordinates. |
| `blank_states_img.gif` | The blank US map used as the game background. |

## Credits

This project follows the US States Game from
[Dr. Angela Yu's 100 Days of Code](https://www.100daysofcode.org/course/100-days-of-code/).