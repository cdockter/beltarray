#!/usr/bin/python
import RPi.GPIO as gpio
import time

LEFTPin = 23
RIGHTPin = 24
PWMFreq = 100

gpio.setmode(gpio.BCM)
gpio.setup(LEFTPin, gpio.OUT)
gpio.setup(RIGHTPin, gpio.OUT)

pwmLeft = gpio.PWM(LEFTPin, PWMFreq)
pwmRight = gpio.PWM(RIGHTPin, PWMFreq)

pwmLeft.start(0)
pwmRight.start(0)

try:
        while 1:
                for dc in range(0, 101, 1):
                        pwmLeft.ChangeDutyCycle(dc)
                        pwmRight.ChangeDutyCycle(100-dc)
                        time.sleep(0.005)
                time.sleep(0.4)
                for dc in range(100, -1, -1):
                        pwmLeft.ChangeDutyCycle(dc)
                        pwmRight.ChangeDutyCycle(100-dc)
                        time.sleep(0.005)
                time.sleep(0.4)

except (KeyboardInterrupt, SystemExit):
        pass
except:
        pass
pwmLeft.stop()
pwmRight.stop()
gpio.cleanup()


