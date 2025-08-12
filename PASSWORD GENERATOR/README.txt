Password Generator

Description:
A Python program that generates secure and customizable passwords. 
You can set the minimum length and choose whether to include numbers 
and special characters.

Features:
- Random password generation
- Option to include/exclude numbers
- Option to include/exclude special characters
- Ensures the password meets chosen criteria

Requirements:
- Python 3.x
- Uses built-in string and random modules

How to Run:
1. Save the script as password_generator.py
2. Open terminal/command prompt in the script's folder
3. Run: python password_generator.py

Example:
password = generate_password(10)              # Letters + numbers + special chars
password = generate_password(10, False)       # Letters + special chars only
password = generate_password(10, False, False) # Letters only
