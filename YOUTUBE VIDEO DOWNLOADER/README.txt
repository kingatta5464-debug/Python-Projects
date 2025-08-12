YouTube Video Downloader (Python)

Description:
------------
This is a Python script that downloads YouTube videos in the highest available resolution
using the pytube library. The user enters a video URL, selects a folder to save the file,
and the script downloads the video there.

Requirements:
-------------
1. Python 3.x installed on your system
2. Required Python packages:
   - pytube
   - tkinter (usually included with Python)

Install pytube if not already installed:
----------------------------------------
pip install pytube

How to Use:
-----------
1. Save the script as youtube_downloader.py (or any name you like).
2. Open a terminal or command prompt in the script's folder.
3. Run:
   python youtube_downloader.py
4. Enter the YouTube video URL when prompted.
5. A folder selection dialog will open — choose where to save the video.
6. The script will download the video in the highest available resolution (MP4 format).

Example:
--------
Enter video url : https://www.youtube.com/watch?v=example
Selected folder is : C:/Users/YourName/Videos
Started Downloading....
Video Downloaded Successfully.

Notes:
------
- This script downloads only a single video at a time (no playlists).
- The selected folder must be valid and writable.
- YouTube’s terms of service apply — download only videos you have rights to.

Author:
-------
Atta Ul Mustafa
