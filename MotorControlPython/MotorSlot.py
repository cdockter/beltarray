from Motor import Motor
import math

class MotorSlot(object):
    def __init__(self, radiansFromAhead, motor):
        self.tou = 2 * math.pi
        self.radiansFromAhead = self.normalize(radiansFromAhead)
        self.motor = motor

    def activate(self, durationInMs):
        self.motor.start(durationInMs)

    def conditinalActivate(self, radiansDirection, radiansArch, durationInMs):
        normalizedDirection = self.normalize(radiansDirection)
        normalizedArch = self.normalize(radiansArch)
        offset = math.atan2(math.sin(self.radiansFromAhead) - math.cos(radiansDirection), math.cos(self.radiansFromAhead) - math.cos(radiansDirection))
        absoluteOffset = math.fabs(self.normalize(offset))
        activated = absoluteOffset < math.fabs(self.normalize(radiansArch))
        if(activated):
            self.motor.start(durationInMs)
        return activated, absoluteOffset
    
    def stop(self):
        self.motor.stop()

    def normalize(self, radians):
        return radians % self.tou