#Projet "Youtube Downloader"

# Module : pytube
import youtube_downloader

urls = ("https://www.youtube.com/watch?v=9bZkp7q19f0", 
        "https://www.youtube.com/watch?v=4fndeDfaWCg",
        "https://www.youtube.com/watch?v=0Gl2QnHNpkA")
for url in urls:
    youtube_downloader.download_video(url)