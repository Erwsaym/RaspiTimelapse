#!/bin/python

from flask import Flask, render_template, Response
from camera import Camera

app = Flask(__name__)
camera = Camera()

INTERVAL = 500
FILETARGET = "/mnt/shared/timelapse/pommefraiche/image_"

@app.route('/')
def index():
	return render_template('index.html')

def gen():
	while True:
		frame = camera.getFrame()
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/frame')
def frame():
	return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

def timelapse():
	frame = 0
	while True:
		currentTime = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
		camera.saveFrame(FILETARGET + str(frame) + _ + currentTime + ".jpg")
		frame = frame + 1
		sleep(INTERVAL)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=False)
