from MotorFactory import MotorFactory
from MotorCollection import MotorCollection
import time
import math


factory = MotorFactory()
motorCollection = MotorCollection(factory.getMotors())

continues = True
while continues:
	command = raw_input("next: ")
	if("q" == command):
		continues = False

	if("w" == command):
		motorCollection.activate(0, math.pi/8, 1000)
	if("a" == command):	
		motorCollection.activate(math.pi/2, math.pi/8, 1000)
	if("d" == command):	
		motorCollection.activate(math.pi* 3/2, math.pi/8, 1000)
	if("s" == command):	
		motorCollection.activate(math.pi, math.pi * 2, 1000)

factory.cleanup()
exit()