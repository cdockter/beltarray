from MotorFactory import MotorFactory
from MotorCollection import MotorCollection
import time
import math

factory = MotorFactory()
motorCollection = MotorCollection(factory.getMotors())

motorCollection.activate(0, 2*math.pi, 1000)
time.sleep(2)

motorCollection.activate(0, math.pi/2, 2000)
time.sleep(3)

motorCollection.activate(math.pi/4, 1, 2000)
time.sleep(3)

motorCollection.activate(math.pi/2, 1, 2000)
time.sleep(3)

motorCollection.activate(math.pi * 3/2, 1, 1000)
time.sleep(2)

motorCollection.activate(math.pi * 14/8, 1, 1000)
time.sleep(2)

print "cleaing up"
factory.cleanup()
exit()