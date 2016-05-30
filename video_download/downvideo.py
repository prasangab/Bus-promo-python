import pafy

url = "https://www.youtube.com/watch?v=0JiKcAeN2-M"
video = pafy.new(url)
streams = video.streams

#for s in streams:
 #   print(s.resolution, s.extension, s.get_filesize(), s.url)

best = video.getbest()

best = video.getbest(preftype="webm")

#filename = best.download(quiet=False)
filename = best.download(filepath = "F:" )
