from pytube import YouTube
import os

url = input("enter your url: ")
path = ""

try:
    video = YouTube(url)
    stream = video.streams.filter(only_audio=True).first()
    outFile = stream.download(path)

    base, ext = os.path.splitext(outFile)
    newFile = base + '.mp3'
    os.rename(outFile,newFile)
except:
    print("try again")
