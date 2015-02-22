import RPi.GPIO as GPIO
import math
from Motor import Motor
from MotorSlot import MotorSlot


class MotorFactory(object):
	def __init__(self):
		self.gpio = GPIO
		self.gpio.cleanup()
		self.gpio.setmode(self.gpio.BCM)

	def cleanup(self):
		self.gpio.cleanup()

	def getMotors(self):
		motors = []
		motors.append(MotorSlot(math.pi/8, Motor(17, self.gpio)))
		motors.append(MotorSlot(math.pi * 15/8, Motor(27, self.gpio)))
		motors.append(MotorSlot(math.pi * 1/4, Motor(22, self.gpio)))
		motors.append(MotorSlot(math.pi * 5/4, Motor(23, self.gpio)))
		# motors.append(Motor(24, self.gpio))
		# motors.append(Motor(25, self.gpio))
		return motors
		