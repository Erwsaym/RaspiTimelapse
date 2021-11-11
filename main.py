#!/bin/python3

from flask import Flask, Response
from camera import Camera
from time import sleep
from datetime import datetime
import os
import threading

app = Flask(__name__)
camera = Camera()

INTERVAL = 500 # Time in second each time we want to take a photo
FILETARGET = "/mnt/shared/PATH" # Directory where to save photo

@app.route('/')
def index():
	return "Srv"

def gen():
	while True:
		frame = camera.getFrame()
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/frame')
def frame():
	return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

def timelapse():
	currentTime = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
	path = FILETARGET + "/" + currentTime + "/"
	os.mkdir(path)

	while True:
		currentTime = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
		camera.saveFrame(path + currentTime + ".jpg")
		sleep(INTERVAL)

if __name__ == '__main__':
	t = threading.Thread(target=timelapse)
	t.start()
	app.run(host='0.0.0.0', debug=False)
