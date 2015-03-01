import math

class MockMotor(object):
    def activate(self, durationInMs):
        return

class MotorCollection(object):
    def __init__(self, motors):
        self.motors = motors

    def activate(self, radiansPosition, radiansArch, durationInMs):
        activated = False
        closestMotor = MockMotor()
        closestOffset = 8*math.pi 
        for motor in self.motors:
            activate, offset = motor.conditinalActivate(radiansPosition, radiansArch, durationInMs)
            activated |= activate
            if(closestOffset > offset):
                closestOffset = offset
                closestMotor = motor;
        if(not activated):
            closestMotor.activate(durationInMs)

    def stop(self):
        for motor in self.motors:
            motor.stop()