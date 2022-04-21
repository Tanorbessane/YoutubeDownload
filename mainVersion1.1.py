#Projet "Youtube Downloader"

# Module : pytube

from pytube import YouTube
import  ffmpeg
import os
#Recupération de l'URL

#--------______----------

BASE_YOUTUBE_URL = "youtube.com"
def get_video_url_from_user():
    url =  input("Veuillez enter votre URL youtube : ")
    #On peut aussi tester si un debut d'une phrase avec : startwith()
    if url.lower()[: len(BASE_YOUTUBE_URL)] != BASE_YOUTUBE_URL:
        print("ERROR: veuiller entrer un lien Youtube !!!")
        return get_video_url_from_user()
    return url


url = "youtube.com/watch?v=9bZkp7q19f0"
#url = get_video_url_from_user()


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_download = stream.filesize - bytes_remaining
    percent = bytes_download * 100 / stream.filesize
    print(f"Pregression du Téléchargement : {int(percent)}%")

def get_stream_itag_from_user(streams):
    print("CHOIX DES RESOLUTIONS : ")
    for choix, stream in enumerate(streams, start=1):
        print(f" {choix} - {stream.resolution}")
    #stream = youtube_video.streams.get_by_itag(18)

    while True:

        res_num = input("Choisissez une résolution : ")
        if res_num == "":
            print("ERRROR : Vous devez rentrer un nombre")
        else:
            try:
                res_num_int = int(res_num)
            except Exception:
                print("ERRROR : Vous devez rentrer un nombre")
            else:
                if not 1 <= res_num_int <= len(streams):
                    print(f"ERRROR : Vous devez rentrer un nombre entre 1 et {len(streams)}")
                else:
                    return streams[res_num_int-1].itag


#itag = streams[res_num_int-1].itag

youtube_video = YouTube(url)
youtube_video.register_on_progress_callback(on_download_progress)

print(f"TITRE : {youtube_video.title}")
print(f"NBRE-DE-VUE : {youtube_video.views}")

print("")


print("STREAMS")
streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="video").order_by('resolution').desc()
video_stream = streams[0]

streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
audio_stream = streams[0]
#for stream in streams:
#    print(stream)
print(f"Video stream {video_stream}")
print(f"Audio stream {audio_stream}")
#stream = youtube_video.streams.get_highest_resolution()
#itag = get_stream_itag_from_user(streams)
#print(itag)
#stream = youtube_video.streams.get_by_itag(itag)
print("Téléchargement Video encours ...")
video_stream.download("video")
print("Téléchargement Terminé")
print("Téléchargement Audio encours ...")
audio_stream.download("audio")
print("Téléchargement Terminé")

audio_filename= os.path.join("audio",audio_stream.default_filename)
video_filename=os.path.join("video",video_stream.default_filename)
output_filename = video_stream.default_filename

ffmpeg.output(ffmpeg.input(audio_filename),ffmpeg.input(video_filename),output_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True)