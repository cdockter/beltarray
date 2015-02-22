class MotorCollection(object):
	def __init__(self, motors):
		self.motors = motors

	def activate(self, radiansPosition, radiansArch, durationInMs):
		for motor in self.motors:
			motor.conditinalActivate(radiansPosition, radiansArch, durationInMs)

	def stop(self):
		for motor in self.motors:
			motor.stop()