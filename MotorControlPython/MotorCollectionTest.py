from MotorFactory import MotorFactory
from MotorCollection import MotorCollection
import time

factory = MotorFactory()
motorCollection = MotorCollection(factory.getMotors())

motorCollection.activate(0, 7, 500)

time.sleep(6)
print "cleaing up"
factory.cleanup()
exit()