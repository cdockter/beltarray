import threading

class Motor(object):
	def __init__(self, id, gpio):
		self.id = id
		self.gpio = gpio
		self.gpio.setup(id, gpio.OUT)

	def start(durationInMs):
		self.gpio.output(self.id, True)
		threading.Timer(durationInMs*1000, self.stop).start()

	def stop():
		self.gpio.output(self.id, False)

		