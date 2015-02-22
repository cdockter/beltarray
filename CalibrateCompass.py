#!/usr/bin/python
import smbus
import time
import math

bus = smbus.SMBus(1)
address = 0x1e


def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def write_byte(adr, value):
    bus.write_byte_data(address, adr, value)

write_byte(0, 0b01110000) # Set to 8 samples @ 15Hz
write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
write_byte(2, 0b00000000) # Continuous sampling

x_min = read_word_2c(3)
y_min = read_word_2c(7)
z_min = read_word_2c(5)
x_max = read_word_2c(3)
y_max = read_word_2c(7)
z_max = read_word_2c(5)

try:
    while True:
        x = read_word_2c(3)
        y = read_word_2c(7)
        z = read_word_2c(5)
        x_max = max(x_max, x)
        y_max = max(y_max, y)
        z_max = max(z_max, z)
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        z_min = min(z_min, z)

        print "x    : ", x,     "y    : ", y,     "z: ", z
        print "x max: ", x_max, "y max: ", y_max, "z: ", z_max
        print "x min: ", x_min, "y min: ", y_min, "z: ", z_min
        time.sleep(0.1)
except:
    pass

print "FINAL:"
print "x max: ", x_max, "y max: ", y_max, "z: ", z_max
print "x min: ", x_min, "y min: ", y_min, "z: ", z_min
