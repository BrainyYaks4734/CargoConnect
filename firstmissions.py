from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

motors = MotorPair('A', 'B')
motors.set_default_speed(50)

def gyroTurn(degrees, speed):
    if (degrees < 0):
        hub.motion_sensor.reset_yaw_angle()
        angle = hub.motion_sensor.get_yaw_angle()
        motors.start(-100,speed)
        while angle>degrees:
            angle = hub.motion_sensor.get_yaw_angle()
        motors.stop()
    else:
        hub.motion_sensor.reset_yaw_angle()
        angle = hub.motion_sensor.get_yaw_angle()
        motors.start(100, speed)
        while angle<degrees:
            angle = hub.motion_sensor.get_yaw_angle()
        motors.stop()
#motors.move(70)
#gyroTurn(90, 20)
#motors.move(10)
#wait_for_seconds(3) #flip the engine to the battery cell.
#motors.move(-15)
#gyroTurn(-90, 20)
#motors.move(-20)
#gyroTurn(-45, 20)
gyroTurn(45, 20)
