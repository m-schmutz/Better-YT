#!./env/bin/python3

from lib.ytdlp import get_video_metadata, download_video



resonanceUrl = 'https://www.youtube.com/watch?v=8GW6sLrK40k'

url = 'https://www.youtube.com/watch?v=T-VZ1kL8ZgE&t'
# url = 'https://www.youtube.com/watch?v=T-VZ1kLasdE&t'



meta = get_video_metadata(url)


print(meta)

download_video(resonanceUrl, 'resonance.mp4')



