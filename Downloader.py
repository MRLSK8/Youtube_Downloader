from pytube import YouTube

yt = YouTube(str(input("Enter the video link: ")))

videos = yt.streams.filter(subtype='mp4').all()  # Gets all download options

print("\n")
counter = 1
for types in videos:
    print(str(counter) + ". "+str(types))
    counter += 1

quality = int(input("\nEnter the number of the video: "))
qualityChosen = videos[quality - 1]

destination = str(input("Enter the destination: "))

print("\n Wait, downloading ...\n")

qualityChosen.download(destination) #Download the video

print("\n Video: " + yt.title + "\n Has been successfully downloaded ")