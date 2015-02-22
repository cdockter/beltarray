from Motor import Motor
import math

class MotorSlot(object):
	def __init__(self, radiansFromAhead, motor):
		self.tou = 2 * math.pi
		self.radiansFromAhead = self.normalize(radiansFromAhead)
		self.motor = motor
	
	def conditinalActivate(self, radiansPosition, radiansArch, durationInMs):
		maxPosition = self.normalize(radiansPosition + (radiansArch/2))
		minPosition = self.normalize(radiansPosition - (radiansArch/2))

		motorPosition = self.radiansFromAhead

		print "max: " + str(maxPosition)
		print "min: " + str(minPosition)
		print "current position: " + str(motorPosition)
		if(motorPosition > minPosition and motorPosition < maxPosition):
			self.motor.start(durationInMs)
	
	def stop(self):
		self.motor.stop()

	def normalize(self, radians):
		if(radians > math.pi):
			return math.pi - radians
		if(radians < (-1 * math.pi)):
			return radians + math.pi
		return radians