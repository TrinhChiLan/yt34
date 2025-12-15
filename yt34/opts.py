import ffmpeg_resolve

mp3_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
}

mp4_opts = {
    'format': "mp4",
}

if ffmpeg_resolve.use_bundled:
    mp3_opts['ffmpeg_location'] = "./ffmpeg"
    mp4_opts['ffmpeg_location'] = "./ffmpeg"