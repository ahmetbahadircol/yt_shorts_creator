from pytube import YouTube

#link = input("Link: ")
link = "https://www.youtube.com/shorts/GGJPsZxLCXc"

yt = YouTube(link)
video = yt.streams.get_highest_resolution()
video.download()