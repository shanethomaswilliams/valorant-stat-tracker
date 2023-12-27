import cv2
import time
from pytube import YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 

print("PyTube Download Time Check:")
print("  Youtube URL: https://www.youtube.com/watch?v=JNYJjntEfRg&ab_channel=VALORANTChampionsTour")


# Create youtube object to pull the stream from
yt = YouTube("https://www.youtube.com/watch?v=JNYJjntEfRg&ab_channel=VALORANTChampionsTour")

# Get the stream with the highest resolution
video_stream = yt.streams.get_highest_resolution()
frame_rate = yt.streams.get_highest_resolution().fps

# Read the video file
cap = cv2.VideoCapture(video_stream.url)

# Get the total number of frames in the video
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("  Total Frames: ", num_frames)
print("  Total Seconds:  ", num_frames / frame_rate, "\n")


times = []

for i in range(5):
    # Get Start time for Measuring
    start_time = time.time()

    # Load frames into a list
    frame_buffer = [None] * (20 * 60 * frame_rate)
    for i in range(20 * 60 * frame_rate):
        ret, frame = cap.read()
        if not ret:
            break
        frame_buffer[i] = frame

    # Finding end time
    end_time = time.time()
    print("  20 Minute Download Time: {} secs".format(end_time - start_time))
    times.append(end_time - start_time)

print("\nAverage Download Time:  {} secs".format(sum(times) / len(times)))
num_twenty_mins = (num_frames / frame_rate) / (20 * 60)
(t_min, t_sec) = divmod(num_twenty_mins * (sum(times) / len(times)), 60)
print("Time For Total Video: ", round(t_min),":",round(t_sec))

# Close the video file
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()