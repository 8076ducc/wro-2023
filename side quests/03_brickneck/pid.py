from pybricks.tools import wait
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
        self.left=0,
        self.right=0,
        self.current_speed = 0
        self.lines_passed = 0

    def reset_values(self):
        self.proportional = 0
        self.integral = 0
        self.derivative = 0
        self.last_error = 0
        self.current_speed = 0
        self.lines_passed = 0

        
class LineTrack(PID):
    def __init__(self):
        PID.__init__(self)

    def track(
        self,
        left_th,
        right_th,
        lines,
        direction = 1,
        speed: float = 800,
        rotation = 360,
        left_sensor = left_cs_f,
        right_sensor = right_cs_f,
        reset=True,
        kp=1.5,
        ki=0,
        kd=0,
    ):
        self.accel = 25
        speed = speed * direction

        if reset == True:
            self.reset_values()

        if speed > 0:
            kp = 1.2

        while self.lines_passed < lines:
            if (left_sensor.reflection() < 20 and right_sensor.reflection() < 20):
                self.lines_passed += 1
                if self.lines_passed < lines:
                    ev3.speaker.beep(duration=50)
                    # if self.lines_passed == lines - 1:
                    #     angle = abs(base.angle())
                    # wait(50)

            self.error = (
                - (left_th - left_sensor.reflection())
                + ((right_th - right_sensor.reflection()))
            )
            self.proportional = self.error * kp
            self.integral += self.error
            self.derivative = (self.error - self.last_error) * kd

            self.correction = self.proportional + (self.integral * ki) + self.derivative

            if self.current_speed < abs(speed): 
                self.current_speed += self.accel * 0.1
            # elif self.lines_passed == lines - 1 and abs(base.angle()) > rotation + angle:
            #     self.current_speed -= self.accel * 0.1
            #     ev3.speaker.beep(100, 50)

            self.base.run(
                (speed + (self.correction)) * (self.current_speed / abs(speed)),
                (speed - (self.correction))  * (self.current_speed / abs(speed)),
            )

            self.last_error = self.error
        
        base.brake()
        # ev3.speaker.beep(700, 100)

line_track = LineTrack()