#!/usr/bin/env python3

import cv2 
from pytube import YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 
from tqdm import tqdm
import json

def download_videos():
    with open('./config/training_data_urls.json') as data_file:    
        data = json.load(data_file)

    print("Downloading YouTube URLS...")
    for yt_url in data['data']:
        yt = YouTube(yt_url, on_progress_callback=on_progress)
        videos = yt.streams.get_highest_resolution()
        output_path = './data'
        print("Current Download: ", yt.title)
        videos.download(output_path=output_path)
    print("Complete :)")

def test_time_for_local(url: str):
    yt = YouTube(url)

    # Get the stream with the highest resolution
    video_stream = yt.streams.get_highest_resolution()

    # Open the video stream
    cap = cv2.VideoCapture(video_stream.url)

    # Variables for frame navigation
    current_frame = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    buffer_size = 1000  # Number of frames to preload

    # Preload frames into a list
    frame_buffer = [None] * buffer_size
    for i in range(buffer_size):
        ret, frame = cap.read()
        if not ret:
            break
        frame_buffer[i] = frame

    # Create a function to update the current frame based on the slider position
    def on_slider_change(pos):
        global current_frame
        current_frame = pos

    # Create a window and a trackbar (slider)
    cv2.namedWindow('Video Frame')
    cv2.createTrackbar('Frame', 'Video Frame', 0, 3000, on_slider_change)

    while True:
         # Get the current position of the trackbar
        pos = cv2.getTrackbarPos('Position', 'video')
        # Update the frame buffer if needed
        if pos % buffer_size == 0 and current_frame != 0:
            ret, frame = cap.read()
            if not ret:
                break
            frame_buffer[current_frame % buffer_size] = frame

        # Display the current frame
        cv2.imshow('Video Frame', frame_buffer[current_frame % buffer_size])

        # Display frame information
        cv2.putText(frame_buffer[current_frame % buffer_size], f'Frame {current_frame + 1}/{total_frames}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Update the trackbar position
        cv2.setTrackbarPos('Frame', 'Video Frame', current_frame)

        # Wait for key press
        key = cv2.waitKey(50) & 0xFF

        # Move to the next frame on arrow key press
        if key == ord('d'):  # Right arrow key code
            print("typed d")
            current_frame += 1
        elif key == ord('a'):  # Left arrow key code
            print("typed a")
            current_frame = max(0, current_frame - 1)

        # Break the loop if 'q' key is pressed
        elif key == ord('q'):
            break

        # Update the frame buffer if needed
        if current_frame % buffer_size == 0 and current_frame != 0:
            ret, frame = cap.read()
            if not ret:
                break
            frame_buffer[current_frame % buffer_size] = frame

    # Release the video capture object and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()


test_time_for_local("https://www.youtube.com/watch?v=JNYJjntEfRg&ab_channel=VALORANTChampionsTour")