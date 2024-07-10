from pytube import YouTube
import os

print(os.getcwd())

link = input("Link: ")

yt = YouTube(link)
video = yt.streams.get_highest_resolution()

video.download("/Users/ahmetcol/Downloads/randm")