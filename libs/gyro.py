from math import *

motors = MotorPair('A', 'B')
motors.set_default_speed(100)
def gyroCW(degrees):
    hub.motion_sensor.reset_yaw_angle()
    angle = hub.motion_sensor.get_yaw_angle()
    motors.start(100,20)
    while angle<degrees:
        angle = hub.motion_sensor.get_yaw_angle()
    motors.stop()
def gyroCCW(degrees):
    hub.motion_sensor.reset_yaw_angle()
    angle = hub.motion_sensor.get_yaw_angle()
    motors.start(-100,20)
    while angle>degrees:
        angle = hub.motion_sensor.get_yaw_angle()
    motors.stop()

def gyro(degrees):
    if (degrees < 0):
        gyroCCW(degrees)
    else:
        gyroCW(degrees)
