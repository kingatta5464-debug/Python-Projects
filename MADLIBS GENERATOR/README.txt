Story Filler (Mad Libs Game)
============================

Description:
------------
This Python program reads a story from a text file (`story.txt`) that contains placeholders 
enclosed in angle brackets (e.g., <noun>, <verb>, <adjective>). The player is prompted to 
enter words to replace these placeholders, and the completed story is displayed.

Features:
---------
- Reads a pre-written story from `story.txt`.
- Detects placeholders between `<` and `>` automatically.
- Prompts the user for input to fill each placeholder.
- Replaces all placeholders with the provided words to create a custom story.
- Fun way to practice string manipulation, file handling, and loops.

How to Prepare:
---------------
1. Create a file named `story.txt` in the same directory as the script.
2. Write a story inside it with placeholders, for example:
Today I went to the <place>. I saw a <adjective> <animal>.
It was <verb> all day long!

mathematica
Copy
Edit

How to Run:
-----------
1. Ensure Python (version 3.x) is installed.
2. Save the script as `story_filler.py`.
3. Open the terminal or command prompt in the project’s folder.
4. Run:
python story_filler.py

Example:
--------
story.txt content:
------------------
Today I went to the <place>. I saw a <adjective> <animal>.  
It was <verb> all day long!

Program output:
---------------
Enter a word for <place> : park  
Enter a word for <adjective> : happy  
Enter a word for <animal> : dog  
Enter a word for <verb> : running  

Today I went to the park. I saw a happy dog.  
It was running all day long!

Author:
-------
Atta Ul Mustafa