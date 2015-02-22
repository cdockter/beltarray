import threading

class Motor(object):
	def __init__(self, id, gpio):
		self.id = id
		self.gpio = gpio
		self.gpio.setup(id, gpio.OUT)

	def start(self, durationInMs):
		print "activting motor"
		self.gpio.output(self.id, True)
		threading.Timer(durationInMs*1000, self.stop).start()

	def stop(self):
		print "deactivating motor"
		self.gpio.output(self.id, False)

		