from Motor import Motor

class MotorSlot(object):
	def __init__(self, radiansFromAhead, motor):
		self.radiansFromAhead = radiansFromAhead
		self.motor = motor
	
	def conditinalActivate(self, radiansPosition, radiansArch, durationInMs):
		maxPosition = radiansPosition - (radiansArch/2)
		minPosition = radiansPosition + (radiansArch/2)
		print "max: " + str(maxPosition)
		print "min: " + str(minPosition)
		print "current position: " + str(radiansPosition)
		if(self.radiansFromAhead > minPosition and self.radiansFromAhead < maxPosition):
			self.motor.start(durationInMs)
	
	def stop(self):
		self.motor.stop()