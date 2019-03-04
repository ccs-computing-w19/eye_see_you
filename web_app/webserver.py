from flask import Flask, redirect, url_for, session, request, jsonify, Markup, flash, render_template, Response
from camera import VideoCamera

app = Flask(__name__)

# Change this to false in production
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

if __name__ == '__main__':
    app.run()
