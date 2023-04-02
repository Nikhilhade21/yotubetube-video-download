import pytube

url = input("hi")

path="D:\Animated Movies"

pytube.YouTube("https://youtu.be/sTq_Z4xZNvM").streams.get_highest_resolution().download(path)
