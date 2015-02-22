import MotorFactory

factory = MotorFactory()
motorCollection = MotorCollection(factory.getMotors())

motorCollection.activate(0, 6, 2)

sleep(4)
factory.cleanup()
