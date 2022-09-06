from pytube import YouTube

link = input("Past Your Link here: ").strip()

yt_link = YouTube(link)

# Title of video
print("Title: ", yt_link.title)
# Number of views of video
print("Number of views: ", yt_link.views)
# Length of the video
print("Length of video: ", yt_link.length, " mintues")
# Description of video
print("Description: ", yt_link.description)
# Rating
print("Ratings: ", yt_link.rating)

# getting highest stream

youtube_stream = yt_link.streams.get_highest_resolution()

# finally downloading the video

youtube_stream.download()
