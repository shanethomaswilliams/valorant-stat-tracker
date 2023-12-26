from flask import Flask, request,jsonify
from flask_socketio import SocketIO,emit
from flask_cors import CORS
from pytube import YouTube
import cv2
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")

@socketio.on("connect")
def connected():
    global video_stream, cap
    """event listener when client connects to the server"""
    print("client has connected")
    socketio.emit("/connect", "You've connected to the server!")

@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("/disconnect",f"user {request.sid} disconnected",broadcast=True)

@socketio.on("video_url")
def handle_video_url(url):
    print("received video_url: '", str(url).strip(),"'")
    global video_stream, cap

    try:
        video = YouTube(str(url))
        print(video)
        stream = video.streams.get_highest_resolution()
        cap = cv2.VideoCapture(stream.url)
        send_frames_in_packs(cap)  # Send frames in packs
    except Exception as e:
        socketio.emit("/error", data={"message": f"Error opening video: {e}"})

def send_frames_in_packs(cap):
    print("Processing video")
    frames = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow("video", frame)
        if not frame:
            print("Video Ending... closing connection")
            # End of video, emit a signal to close the socket
            socketio.emit("/video_ended", data={"message": f"Video has completed!"})
            break
        if not ret:
            break  # End of video

        ret, jpg_buffer = cv2.imencode(".jpg", frame)
        encoded_string = base64.b64encode(jpg_buffer).decode("utf-8")
        print('sending frame...')
        socketio.emit("frame", data=encoded_string)

if __name__ == '__main__':
    socketio.run(app, debug=True,port=5001)