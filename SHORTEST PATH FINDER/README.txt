Maze Pathfinding Visualization (Python + Curses)

Description:
------------
This program demonstrates a Breadth-First Search (BFS) pathfinding algorithm
inside a maze, visualized in the terminal using Python's 'curses' module.
The maze is represented as a 2D list, with:
  - '#' representing walls
  - 'O' as the starting point
  - 'X' as the destination
  - ' ' (space) as open paths

The BFS algorithm searches for the shortest path from the start ('O') to
the end ('X'), highlighting the path in red as it searches.

How It Works:
-------------
1. The maze layout is predefined in a 2D list.
2. The `find_start()` function locates the starting position.
3. The `find_path()` function:
    - Uses BFS to explore all possible paths.
    - Keeps track of visited nodes to avoid loops.
    - Displays the maze in the terminal with each search step.
4. The final path to 'X' is shown in red.

Controls:
---------
- The program automatically starts when run.
- The animation pauses for 0.2 seconds between each search step.
- Press any key to exit after the search completes.

Requirements:
-------------
- Python 3.x
- 'curses' library (already included in most Unix-based Python installations; 
  for Windows, install `windows-curses` via pip)

Run Instructions:
-----------------
1. If using Windows, install curses:
      pip install windows-curses

2. Run the program:
      python maze_solver.py

3. Watch the maze search animation in the terminal.

Notes:
------
- This is a basic BFS maze solver visualization.
- You can modify the maze layout in the 'maze' variable.
- Reduce `time.sleep(0.2)` for faster animation.

Author:
-------
Atta Ul Mustafa
