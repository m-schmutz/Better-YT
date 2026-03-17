#!./env/bin/python3

from subprocess import run, check_output

result = run(['which', 'asdf'], capture_output=True, text=True)
result = check_output(['which', 'asdf'])

# https://www.youtube.com/watch?v=T-VZ1kL8ZgE&t

# print("STDOUT:", result.stdout)
# print("STDERR:", result.stderr)
# print("Return code:", result.returncode)
# python3 yt-dlp --js-runtimes "deno:/home/msch/Projects/Better-YT/binaries/deno" --print "%(title)s\n%(uploader)s\n%(upload_date)s\n%(duration)s" "https://www.youtube.com/watch?v=T-VZ1kL8ZgE&t"



# python3 yt-dlp --js-runtimes "deno:/home/msch/Projects/Better-YT/binaries/deno" --print-json "{thumbnail: .thumbnail, fulltitle: .fulltitle, original_url: .original_url}" "https://www.youtube.com/watch?v=T-VZ1kL8ZgE&t"

# python3 yt-dlp --js-runtimes "deno:/home/msch/Projects/Better-YT/binaries/deno" -J "https://www.youtube.com/watch?v=T-VZ1kL8ZgE&t"
# python3 yt-dlp --js-runtimes "deno:/home/msch/Projects/Better-YT/binaries/deno" -J "https://www.youtube.com/@EmperorLemon"

# python3 yt-dlp --js-runtimes yt-dlp --skip-download --print "%(thumbnail)s" "https://www.youtube.com/@LinusTechTips"\\


# python3 yt-dlp --js-runtimes "deno:/home/msch/Projects/Better-YT/binaries/deno" --skip-download --print "%(thumbnail)s" "https://www.youtube.com/@LinusTechTips"

# https://www.youtube.com/feeds/videos.xml?channel_id=UC7Ucs42FZy3uYzjrqzOIHsw


'''
fields to get:
thumbnail 
fulltitle
original_url



'''