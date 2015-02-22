from Motor import Motor
import math

class MotorSlot(object):
	def __init__(self, radiansFromAhead, motor):
		self.radiansFromAhead = radiansFromAhead
		self.motor = motor
	
	def conditinalActivate(self, radiansPosition, radiansArch, durationInMs):
		tou = 2 * math.pi
		maxPosition = (radiansPosition + (radiansArch/2)) + tou
		minPosition = (radiansPosition - (radiansArch/2)) + tou

		motorPosition = tou + self.radiansFromAhead

		print "max: " + str(maxPosition)
		print "min: " + str(minPosition)
		print "current position: " + str(motorPosition)
		if(motorPosition > minPosition and motorPosition < maxPosition):
			self.motor.start(durationInMs)
	
	def stop(self):
		self.motor.stop()