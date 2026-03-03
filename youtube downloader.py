import yt_dlp

url = "https://youtu.be/ZvYluToZvnA?si=8LYS7kv49C4tJh5X"

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
