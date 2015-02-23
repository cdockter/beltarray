from Motor import Motor
import math

class MotorSlot(object):
	def __init__(self, radiansFromAhead, motor):
		self.tou = 2 * math.pi
		self.radiansFromAhead = self.normalize(radiansFromAhead)
		self.motor = motor
	
	def conditinalActivate(self, radiansDirection, radiansArch, durationInMs):
		normailzedDirection = self.nomralize(radiansDirection)
		normalizedArch = self.normalize(radiansArch)
		offset = normalize((self.radiansFromAhead - normailzedDirection) - normalizedArch/2)

		print "offect: " + str(offset)
		print "direction: " + str(normailzedDirection)
		print "motor position: " + str(self.radiansFromAhead)

		if(offset < radiansArch):
			self.motor.start(durationInMs)

		#if(motorPosition > minPosition and motorPosition < maxPosition ):
		#	self.motor.start(durationInMs)
	
	def stop(self):
		self.motor.stop()

	def normalize(self, radians):
		if(radians > self.tou):
			return self.normalize(radians - self.tou)
		if(radians < 0):
			return self.normalize(radians + self.tou)
		return radians