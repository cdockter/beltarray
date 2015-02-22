from MotorFactory import MotorFactory
from MotorCollection import MotorCollection
import time

factory = MotorFactory()
motorCollection = MotorCollection(factory.getMotors())

motorCollection.activate(0, 6, 2)

time.sleep(4)
factory.cleanup()
