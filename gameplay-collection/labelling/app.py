#!/usr/bin/env python3

import os
import re
from flask import Flask, render_template, request, send_from_directory
import requests
from io import BytesIO

app = Flask(__name__)

# Define a folder to store temporary images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def validate_youtube_url(youtube_url):
    regex = r'(https?://)?(www\.)?(youtube|youtu\.be)/(watch\?v=|embed/)?([A-Za-z0-9_\-]+)'
    match = re.match(regex, youtube_url)
    return match is not None

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/display', methods=['POST'])
def display():
    youtube_url = request.form.get('image_url')

    # Validate the YouTube URL
    if not validate_youtube_url(youtube_url):
        return "Please provide a valid YouTube Video url:"

    # Extract the video ID from the YouTube URL
    video_id = youtube_url.split('/')[-1]

    # Render the display.html template, passing in the video ID
    return render_template('display.html', video_id=video_id)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)


