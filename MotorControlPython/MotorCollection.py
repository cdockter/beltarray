class MotorCollection(object):
	def __init__(self, motors):
		self.motors = motors

	def activate(radiansPosition, radiansArch, durationInMs):
		for motor in self.motors:
			motor.conditinalActivate(radiansPosition, radiansArch, durationInMs)

	def stop():
		for motor in self.motors:
			motor.stop()