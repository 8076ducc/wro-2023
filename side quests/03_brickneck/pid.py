from devices import *

def abscap(x, cap):
    if (x > abscap):
        return abscap
    elif (x < -abscap):
        return -abscap
    else:
        return x

class PID(object):
    def __init__(
        self,
    ):
        self.base = base
        self.proportional = 0
        self.integral = 0
        self.derivative = 0
        self.error = 0
        self.last_error = 0
        self.correction = 0
        self.left=0,
        self.right=0,
        self.loop = 0

    def reset_values(self):
        self.proportional = 0
        self.integral = 0
        self.derivative = 0
        self.last_error = 0
        self.loop = 0

class LineTrack(PID):
    def __init__(self):
        PID.__init__(self)

    def track(
        self,
        speed: float,
        left_th,
        right_th,
        condition=lambda: True,
        left_sensor = left_cs_f,
        right_sensor = right_cs_f,
        reset=True,
        kp=0,
        ki=0,
        kd=0,
        slew=0,
    ):
        if reset == True:
            self.reset_values()

        while condition():
            self.error = (
                - (left_th[0] - left_sensor.rgb()[0])
                - (left_th[1] - left_sensor.rgb()[1])
                - (left_th[2] - left_sensor.rgb()[2])
                + (right_th[0] - right_sensor.rgb()[0])
                + (right_th[1] - right_sensor.rgb()[1])
                + (right_th[2] - right_sensor.rgb()[2])
            )
            self.proportional = self.error * kp
            self.integral += self.error
            self.derivative = (self.error - self.last_error) * kd

            self.correction = (self.integral * ki) + self.proportional + self.derivative

            left_change = (speed + self.correction) - self.left
            self.left += abscap(left_change, slew)
            right_change = (speed - self.correction) - self.right
            self.right += abscap(right_change, slew)

            self.base.run(
                self.left,
                self.right,
            )

            self.loop += 1
            self.last_error = self.error

line_track = LineTrack()