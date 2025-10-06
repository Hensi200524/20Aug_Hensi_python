from pytubefix import YouTube

url = "https://www.youtube.com/watch?v=tfh6cd8AauQ"

# Create YouTube object
yt = YouTube(url)

# Get highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()

print("✅ Download complete!")
