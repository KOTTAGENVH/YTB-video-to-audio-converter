import yt_dlp
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

allowed_qualities = {"320", "128", "96", "64"}

while True:
    quality = input(
        "Please enter the audio quality (320 / 128 / 96 / 64): "
    ).strip()

    if quality in allowed_qualities:
        break

    print(
        "Sorry, we only support:\n"
        "320 = max\n"
        "128 = excellent\n"
        "96  = very good\n"
        "64  = good (clear voice)\n"
    )
        
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'), 
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': quality, #320 is max 128 is excellent 96 is Very good 64 is good at Clear voice
    }],
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    },
    'geo_bypass': True,  # Bypass geographic restriction
}

def download_audio(link):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return f"Download completed: {link}"
    except Exception as e:
        return f"Error downloading {link}: {e}"


links = []
print("Enter YouTube links (press ENTER on empty line to start downloading):")


while True:
    link = input()
    if not link:
        break
    links.append(link)

# Run downloads with multithreading (3 at a time)
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(download_audio, link) for link in links]

    for future in as_completed(futures):
        print(future.result())

print("\nAll downloads finished. Files are saved in your Downloads folder.")
