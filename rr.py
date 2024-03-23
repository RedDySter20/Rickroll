import os
import sys
from threading import Thread
import ctypes
import pyglet
from moviepy.editor import VideoFileClip
import imageio

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Create directory if it doesn't exist
user_name = os.getlogin()
save_directory = os.path.join("C:\\Users", user_name, "rickroll")

video_filename = os.path.join(save_directory, "video.mp4")
audio_filename = os.path.join(save_directory, "audio.mp3")

video_path = resource_path(video_filename)
audio_path = resource_path(audio_filename)

temp_image_path = 'temp_frame.jpg'
frame_count = 0

def is_64bit_windows():
    try:
        return os.name == 'nt' and os.environ['PROCESSOR_ARCHITECTURE'].endswith('64')
    except AttributeError:
        if 'PROCESSOR_ARCHITEW6432' in os.environ:
            return False
        else:
            return True

def change_bg(path):
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(20, 0, path, 3)

def extract_frame(video_path, temp_image_path, frame_count):
    clip = VideoFileClip(video_path)
    frame = clip.get_frame(frame_count / clip.fps)
    frame_image = temp_image_path
    imageio.imwrite(frame_image, frame)  # Save the frame as an image
    return frame_image

def play_audio():
    sound = pyglet.media.load(audio_path, streaming=False)
    sound.play()
    pyglet.app.run()

Thread(target=play_audio).start()
clip = VideoFileClip(video_path)
while frame_count < clip.duration * clip.fps:
    temp_frame = extract_frame(video_path, temp_image_path, frame_count)
    change_bg(os.path.abspath(temp_frame))
    frame_count += 1