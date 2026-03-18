#!/usr/bin/python3

from lib.ytdlp import update_dlp_environment, get_video_metadata, download_video, download_audio



resonanceUrl = 'https://www.youtube.com/watch?v=LZ4ug8Nc0Q8'



update_dlp_environment()


# metadata = get_video_metadata(resonanceUrl)


# print(metadata)

# download_video(resonanceUrl, 'resonance.mp4')

download_audio(resonanceUrl, 'resonance.mp3')