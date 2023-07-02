#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Color, Button
from pybricks.tools import wait, StopWatch
from devices import *
from pid import *
from constants import *

# while True:
#     if ev3.buttons.pressed():
#         if ev3.buttons.pressed()[0] == Button.CENTER:
#             break

# wait(200)

line_track.track(
    95,
    95,
    2,
)

while True:
    line_track.track(
        70,
        70,
        1,
        direction=-1,
        left_sensor=left_cs_b,
        right_sensor=right_cs_b,
    )

    base.run_target(1500, 1500, 0, -340)

    line_track.track(
        95,
        95,
        1,
    )
    # base.run_target(1500, 1500, 30, 0)

    line_track.track(
        70,
        70,
        3,
        direction=-1,
        left_sensor=left_cs_b,
        right_sensor=right_cs_b,
    )
    # base.run_target(1500, 1500, 25, 0)

    line_track.track(
        95,
        95,
        2,
    )
    
    # base.run_target(1500, 1500, -30, 0)
    # base.run_target(1500, 1500, -35, -35)
    base.run_target(1500, 1500, 0, 380)

    line_track.track(
        95,
        95,
        1,
    )

base.brake()

# line_track.track(
#     90,
#     95,
#     3,
# )

# line_track.track(
#     65,
#     65,
#     3,
#     direction=-1,
#     left_sensor=left_cs_b,
#     right_sensor=right_cs_b,
# )

# while True:
#     ev3.screen.clear()
#     base.run(1500, 1500)
#     ev3.screen.print(base_left.speed(), base_right.speed(), sep=' ', end='\n')
#     wait(1000)
