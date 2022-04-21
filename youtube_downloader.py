#Projet "Youtube Downloader"

# Module : pytube

from pytube import YouTube
import  ffmpeg
import os
#Recupération de l'URL

#--------______----------



def on_download_progress(stream, chunk, bytes_remaining):
    bytes_download = stream.filesize - bytes_remaining
    percent = bytes_download * 100 / stream.filesize
    print(f"Pregression du Téléchargement : {int(percent)}%")

def download_video(url):
    youtube_video = YouTube(url)
    youtube_video.register_on_progress_callback(on_download_progress)

    #print(f"TITRE : {youtube_video.title}")
    #print(f"NBRE-DE-VUE : {youtube_video.views}")

    #print("")


    #print("STREAMS")
    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="video").order_by('resolution').desc()
    video_stream = streams[0]

    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
    audio_stream = streams[0]

   # print(f"Video stream {video_stream}")
   # print(f"Audio stream {audio_stream}")

    print(f"Téléchargement {youtube_video.title} encours ...")
    video_stream.download("video")
    audio_stream.download("audio")

    audio_filename= os.path.join("audio",audio_stream.default_filename)
    video_filename=os.path.join("video",video_stream.default_filename)
    output_filename = video_stream.default_filename

    ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename),output_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True)


    print("Téléchargement Terminé")
    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")