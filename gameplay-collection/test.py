import cv2
from pytube import YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 

# Create youtube object to pull the stream from
yt = YouTube("https://www.youtube.com/watch?v=JNYJjntEfRg&ab_channel=VALORANTChampionsTour")

# Get the stream with the highest resolution
video_stream = yt.streams.get_highest_resolution()

# Read the video file
cap = cv2.VideoCapture(video_stream.url)

# Get the total number of frames in the video
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Set the initial position of the trackbar to 0
pos = 0
cv2.namedWindow('video')
def update_frame(x):
    global cap, pos
    pos = x
    cap.set(cv2.CAP_PROP_POS_FRAMES, pos)
    ret, frame = cap.read()
    cv2.imshow('video', frame)

# Create a trackbar to scrub through the video
cv2.createTrackbar('Position', 'video', 0, 2000, update_frame)

# Display the first frame
ret, frame = cap.read()
cv2.imshow('video', frame)

while True:
    # Check if the user wants to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the video file
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()