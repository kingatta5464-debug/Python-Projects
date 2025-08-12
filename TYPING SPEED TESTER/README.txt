Speed Typing Test
-----------------

Description:
------------
This is a console-based Speed Typing Test game built in Python using the 'curses' library.
It measures how fast you can type a given sentence and calculates your Words Per Minute (WPM).
The game highlights correct letters in green and incorrect letters in red while you type.

Features:
---------
- Randomly selects a sentence from "text_to_test_speed.txt".
- Real-time WPM calculation.
- Highlights correct and incorrect letters.
- Allows backspacing to fix mistakes.
- Simple console interface using 'curses'.

Requirements:
-------------
- Python 3.x
- curses library (pre-installed with Python on Linux/Mac; for Windows, install via `pip install windows-curses`)
- random module (comes pre-installed with Python)
- time module (comes pre-installed with Python)
- A text file named "text_to_test_speed.txt" containing sentences to type.

How to Play:
------------
1. Run the Python file in your terminal.
2. The game will display a welcome screen — press any key to start.
3. Type the displayed sentence as quickly and accurately as you can.
4. Correct letters appear in green; incorrect letters appear in red.
5. Once you finish typing the text, your WPM will be displayed.
6. Press any key to try again or ESC to exit.

Files:
------
- speed_typing_test.py     : The main Python script containing the game code.
- text_to_test_speed.txt   : A text file with one or more sentences for typing practice.
- readme.txt               : This file.

Author:
-------
Created by Atta Ul Mustafa
