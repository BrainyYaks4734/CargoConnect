from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
motors = MotorPair('B', 'C')
lift = Motor ('A')
twist = Motor ('D')
motors.set_default_speed(20)

# startfile libs/gyro.py
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
# endfile libs/gyro.py

# startfile launches/first.py
lift.run_for_degrees(-90)
motors.move(72)
gyroTurn(45, 20)
lift.run_for_degrees(90)
# endfile launches/first.py
