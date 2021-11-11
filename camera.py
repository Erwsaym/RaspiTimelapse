from picamera import PiCamera
from io import BytesIO

class Camera():
	def __init__(self):
		self.camera = PiCamera()

	def saveFrame(self, dst):
		self.camera.capture(dst)

	def getFrame(self):
		stream = BytesIO()
		for _ in self.camera.capture_continuous(stream, 'jpeg', use_video_port=True):
			stream.seek(0)
			return stream.read()
