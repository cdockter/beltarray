from Motor import Motor
import math

class MotorSlot(object):
	def __init__(self, radiansFromAhead, motor):
		self.tou = 2 * math.pi
		self.radiansFromAhead = self.normalize(radiansFromAhead)
		self.motor = motor
	
	def conditinalActivate(self, radiansDirection, radiansArch, durationInMs):
		normalizedDirection = self.normalize(radiansDirection)
		normalizedArch = self.normalize(radiansArch)
		offset = self.normalize((self.radiansFromAhead - normalizedDirection) - radiansArch/2)

		#print "offset: " + str(offset)
		#print "arch" + str(radiansArch)
		#print "direction: " + str(normalizedDirection)
		#print "motor position: " + str(self.radiansFromAhead)

		if(offset < radiansArch or radiansDirection == self.radiansFromAhead):
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