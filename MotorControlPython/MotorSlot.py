class MotorSlot(object):
	def __init__(self, radiansFromAhead, motor):
		self.radiansFromAhead = radiansFromAhead
		self.motor = motor
	
	def conditinalActivate(radiansPosition, radiansArch, durationInMs):
		maxPosition = radiansPosition - (radiansArch/2)
		minPosition = radiansPosition + (radiansArch/2)
		if(self.radiansFromAhead > minPosition and self.radiansFromAhead < maxPosition):
			self.motor.start(durationInMs)
	
	def stop():
		self.motor.stop()