from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    ColorSensor,
)
from pybricks.parameters import Port, Direction, Stop

ev3 = EV3Brick()

base_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
base_right = Motor(Port.C)

base_left.control.limits(1500)
base_right.control.limits(1500)

left_cs_f = ColorSensor(Port.S2)
right_cs_f = ColorSensor(Port.S3)
left_cs_b = ColorSensor(Port.S1)
right_cs_b = ColorSensor(Port.S4)

class Base:
    def __init__(self):
        self.base_left = base_left
        self.base_right = base_right

    def brake(self):
        self.base_left.brake()
        self.base_right.brake()

    def hold(self, motor: Motor = None):
        self.base_left.hold()
        self.base_right.hold()

    def angle(self):
        return (self.base_left.angle() + self.base_right.angle()) / 2

    def reset_angle(self, angle: int = 0):
        self.base_left.reset_angle(angle)
        self.base_right.reset_angle(angle)

    def run(self, left_speed: float, right_speed: float):
        self.base_left.run(left_speed)
        self.base_right.run(right_speed)

    def run_target(self, left_speed, right_speed, left_angle, right_angle):
        base.reset_angle()

        base_left.run_target(left_speed, left_angle, wait=False, then=Stop.HOLD)
        base_right.run_target(right_speed, right_angle, wait=True, then=Stop.HOLD)
        base.brake()

base = Base()
