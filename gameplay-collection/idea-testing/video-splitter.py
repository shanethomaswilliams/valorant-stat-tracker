#!/usr/bin/env python3

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# import module 
import cv2 
import datetime 

## S
SEGMENT_SIZE = 1200

# create video capture object 
data = cv2.VideoCapture('/Users/shanewilliams/Projects/valo_project/loudvfnc/LOUD vs FNC — VCT LOCKIN — Grand Final.mp4') 
  
# count the number of frames 
frames = data.get(cv2.CAP_PROP_FRAME_COUNT) 
fps = data.get(cv2.CAP_PROP_FPS) 
  
# calculate duration of the video in seconds
SECONDS = round(frames / fps)

# Load the video file
video = "/Users/shanewilliams/Projects/valo_project/loudvfnc/LOUD vs FNC — VCT LOCKIN — Grand Final.mp4"

count = 1
for i in range(0, SECONDS, SEGMENT_SIZE):
    ffmpeg_extract_subclip(video, i, min(i + SEGMENT_SIZE, SECONDS), targetname=str('./data/loud_v_fnc_'+str(count)+'.mp4'))
    count += 1