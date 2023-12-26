from flask import Flask, request, abort
from flask_socketio import SocketIO
from pytube import YouTube
import cv2
import base64

app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_my_temporary_secret_key"
socketio = SocketIO(app)

# Declare global variables for stream and capture
video_stream = None
cap = None

@app.route("/")
def index():
    return "<h1>Real-time video labelling</h1>"

@socketio.on("connect")
def handle_connect():
    global video_stream, cap

    # Wait for the video URL to be sent from the frontend

@socketio.on("set_video_url")
def handle_video_url(url):
    global video_stream, cap

    # Disconnect existing stream if any
    if cap:
        cap.release()

    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        cap = cv2.VideoCapture(stream.url)
        socketio.emit("video_info", data={"duration": cap.get(cv2.CAP_PROP_FRAME_COUNT)})
        send_frames_in_packs(cap)  # Send frames in packs
    except Exception as e:
        socketio.emit("error", data={"message": f"Error opening video: {e}"})

def send_frames_in_packs(cap):
    frames = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            # End of video, emit a signal to close the socket
            socketio.emit("video_ended")
            break
        if not ret:
            break  # End of video

        frames.append(frame)
        frame_count += 1

        if frame_count == 50:
            send_pack(frames)
            frames = []
            frame_count = 0

    # Send any remaining frames
    if frames:
        send_pack(frames)

def send_pack(frames):
    encoded_frames = []
    for frame in frames:
        # Resize and encode frame (optional)
        # frame = cv2.resize(frame, frame_size) if frame_size else frame
        ret, jpg_buffer = cv2.imencode(".jpg", frame)
        encoded_string = base64.b64encode(jpg_buffer).decode("utf-8")
        encoded_frames.append(encoded_string)

    socketio.emit("frame_pack", data=encoded_frames)

if __name__ == "__main__":
    socketio.run(app, debug=True)
