
from .paths import DLP_ENV_PY, DLP_ENV_PIP, YT_DLP_PATH, DENO_JS_PATH
from subprocess import run
from json import loads



def get_video_metadata(videoUrl: str):
    
    args = [
        DLP_ENV_PY,
        YT_DLP_PATH,
        '--js-runtimes',
        f'deno:{DENO_JS_PATH}',
        '-J',
        videoUrl
    ]

    result = run(args, capture_output=True, text=True)

    if result.returncode:
        raise RuntimeError(result.stderr)
    
    metadata = loads(result.stdout)

    return (
        metadata['title'],
        metadata['channel'],
        metadata['thumbnail'],
        metadata['original_url'],
        metadata['duration_string']
    )



def download_video(videoUrl: str, filename: str):

    args = [
        DLP_ENV_PY,
        YT_DLP_PATH,
        '--js-runtimes',
        f'deno:{DENO_JS_PATH}',
        '-f',
        'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
        '-o',
        filename,
        videoUrl
    ]