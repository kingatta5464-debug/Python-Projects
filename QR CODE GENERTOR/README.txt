QR Code Generator

Description:
This project contains two Python scripts for generating QR codes.
- QR_code.py: A basic QR code generator.
- advance_QR_code.py: An advanced QR code generator with additional customization options (e.g., colors, logos, image size).

Features:
Basic QR Code Generator (QR_code.py)
- Generates QR codes from user-provided text or URLs.
- Saves generated QR codes as image files.

Advanced QR Code Generator (advance_QR_code.py)
- All features of the basic generator.
- Allows customizing QR code colors.
- Supports embedding a logo in the QR code.
- Adjustable resolution and box size.

Requirements:
- Python 3.x
- qrcode library (install using: pip install qrcode[pil])
- pillow library (install using: pip install pillow)

How to Run:
1. Open terminal/command prompt in the project folder.
2. For basic QR code:
   python QR_code.py
3. For advanced QR code:
   python advance_QR_code.py
4. Follow on-screen instructions to enter the text/URL and customize as needed.

Example (basic):
Enter text or URL: https://www.example.com
QR code saved as example.png

Example (advanced):
Enter text or URL: https://www.example.com
Enter foreground color (e.g., black, #000000): blue
Enter background color (e.g., white, #ffffff): yellow
QR code with custom colors saved as custom_qr.png

Notes:
- Generated QR codes are saved in the same folder as the script.
- Ensure Pillow and qrcode libraries are installed before running.
