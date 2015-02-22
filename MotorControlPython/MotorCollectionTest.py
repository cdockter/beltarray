from MotorFactory import MotorFactory
from MotorCollection import MotorCollection
import time
import math

factory = MotorFactory()
motorCollection = MotorCollection(factory.getMotors())

print "-- all --"
motorCollection.activate(0, 2*math.pi, 1000)
time.sleep(2)

print "-- left front --"
motorCollection.activate(0, math.pi/2, 2000)
time.sleep(3)

print "-- left far --"
motorCollection.activate(math.pi/4, 1.0, 2000)
time.sleep(3)

print "-- right front --"
motorCollection.activate(math.pi/2, 1.0, 2000)
time.sleep(3)

print "-- left all --"
motorCollection.activate(math.pi * 3/2, 1.0, 1000)
time.sleep(2)

print "-- left far --"
motorCollection.activate(math.pi * 14/8, 1.0, 1000)
time.sleep(2)

print "cleaing up"
factory.cleanup()
exit()