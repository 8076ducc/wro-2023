from devices import *

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

            self.base.run(
                speed + (self.correction),
                speed - (self.correction),
            )

            self.loop += 1
            self.last_error = self.error

line_track = LineTrack()