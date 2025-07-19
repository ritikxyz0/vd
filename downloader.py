import yt_dlp
import os

def get_cookie_file(url: str):
    if "instagram.com" in url:
        return 'cookies/cookies_instagram.txt'
    elif "facebook.com" in url or "fb.watch" in url:
        return 'cookies/cookies_facebook.txt'
    elif "youtube.com" in url or "youtu.be" in url:
        return 'cookies/cookies_youtube.txt'
    return None

def download_video_from_url(url: str):
    cookie_file = get_cookie_file(url)
    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True
    }
    if cookie_file and os.path.exists(cookie_file):
        ydl_opts['cookiefile'] = cookie_file

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        return filename
