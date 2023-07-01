#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Color, Button
from pybricks.tools import wait
from devices import *
from pid import *
from constants import *

while True:
    line_track.track(
        800,
        # (9 + 68) / 2,
        95,
        95,
        1,
    )
    base.brake()

    line_track.track(
        -800,
        70,
        70,
        1,
        left_sensor=left_cs_b,
        right_sensor=right_cs_b,
    )
    base.brake()
    wait(50)

    base.run_target(1500, 1500, 0, -360)
    wait(50)

    line_track.track(
        800,
        95,
        95,
        1,
    )
    base.brake()
    wait(100)

    line_track.track(
        -800,
        70,
        70,
        3,
        left_sensor=left_cs_b,
        right_sensor=right_cs_b,
    )
    base.brake()
    wait(50)

    line_track.track(
        800,
        95,
        95,
        2,
    )
    base.brake()
    wait(50)

    base.run_target(1500, 1500, 0, 360)
