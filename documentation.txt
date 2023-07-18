=======================================================
              Insta Mass Downloader
=======================================================

Description:
-------------
This Python script allows you to download all Instagram posts from a given profile URL and save them as a zip file. It utilizes the 'instaloader' library to interact with the Instagram platform and retrieve the posts.

Usage:
--------
1. Ensure you have Python installed on your system.

2. Install the required 'instaloader' library by running the command:
      pip install instaloader

3. Open a terminal or command prompt and navigate to the directory where the script is saved.

4. Run the script using the following command:
      python instamassdownloader.py

5. The script will prompt you to enter the Instagram profile URL. Make sure to provide the complete URL starting with 'https://www.instagram.com/'.

7. The script will download all the posts from the specified Instagram profile and create a zip file in the 'downloads' folder with the username as the filename.

Dependencies:
---------------
- Python 3.x
- instaloader library (install via 'pip install instaloader')

Script Files:
---------------
- instamassdownloader.py

Functions:
------------
- download_instagram_posts(profile_url): This function performs the main logic of downloading the Instagram posts.
  - profile_url (str): The Instagram profile URL to download the posts from.

Example:
-----------
$ python instamassdownloader.py
Enter the Instagram profile URL: https://www.instagram.com/example_profile/
All posts of 'example_profile' have been downloaded and zipped successfully.
The zip file is saved at 'downloads/example_profile.zip'.

Notes:
--------
- Ensure you have the necessary permissions to create folders and write files in the script's directory.
- The script relies on the 'instaloader' library, which interacts with the Instagram platform. Keep in mind that changes to the Instagram API or platform may affect the script's functionality.

