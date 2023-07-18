import instaloader
import os
import shutil

def download_instagram_posts(profile_url):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Set the download directory
    download_dir = 'downloads'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Download the posts
    loader.download_profile(profile_url, profile_pic_only=False)

    # Get the username of the profile
    username = profile_url.split('/')[-2]

    # Rename downloaded files to username
    for filename in os.listdir(download_dir):
        if not filename.startswith(username):
            new_filename = f"{username}_{filename}"
            os.rename(os.path.join(download_dir, filename), os.path.join(download_dir, new_filename))

    # Create a zip file
    zip_path = f'{download_dir}/{username}.zip'
    shutil.make_archive(f"{download_dir}/{username}", 'zip', download_dir)

    print(f"All posts of '{username}' have been downloaded and zipped successfully.")
    print(f"The zip file is saved at '{zip_path}'.")

if __name__ == '__main__':
    # Prompt the user to enter the Instagram profile URL
    profile_url = input("Enter the Instagram profile URL: ")

    # Validate the URL
    if not profile_url.startswith("https://www.instagram.com/"):
        print("Invalid Instagram profile URL. Please make sure it starts with 'https://www.instagram.com/'.")
        exit(1)

    download_instagram_posts(profile_url)
