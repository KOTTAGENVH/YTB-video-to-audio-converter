import yt_dlp
import os

# Get the user's Downloads folder path
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Ask for the link from the user
link = input("Enter the link of the YouTube video you want to download: ")

# Define the download options for audio
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),  # Save in Downloads
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    },
    'geo_bypass': True,  # Bypass geographic restriction
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the audio from the video
        ydl.download([link])
    print("Download completed! The file is saved in your Downloads folder.")
except Exception as e:
    print(f"An error occurred: {e}")
