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
