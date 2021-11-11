from picamera import PiCamera
from time import sleep
from datetime import datetime

interval = 500
frame = 0

camera = PiCamera()

while True:
	currentTime = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
	camera.capture("/mnt/shared/timelapse/pommefraiche/image_" + str(frame) + "_" + currentTime + ".jpg")
	frame = frame + 1
	sleep(interval)
