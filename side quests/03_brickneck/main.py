#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Color, Button
from pybricks.tools import wait
from devices import *
from pid import *
from constants import *

def see_line(thr, left_sensor = left_cs_f, right_sensor = right_cs_f):
    passed = 0

    if (left_sensor.rgb()[0] > BLACK_RGB_LEFT[0] + 5 and right_sensor.rgb()[0] > BLACK_RGB_RIGHT[0] + 5):
        passed += 1

    if passed == thr:
        return True
    else:
        return False

while True:
    # line track from 0 to 1
    LineTrack.track(
        1500,
        [
            ((BLACK_RGB_LEFT[0] + WHITE_RGB_LEFT[0]) / 2),
            ((BLACK_RGB_LEFT[1] + WHITE_RGB_LEFT[1]) / 2),
            ((BLACK_RGB_LEFT[2] + WHITE_RGB_LEFT[2]) / 2),
        ],
        [
            ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
            ((BLACK_RGB_RIGHT[1] + WHITE_RGB_RIGHT[1]) / 2),
            ((BLACK_RGB_RIGHT[2] + WHITE_RGB_RIGHT[2]) / 2),
        ],
        see_line(1),
    )

    base.brake()

    # turn towards 2
    base.run_target(
        1500,
        1500,
        -180,
        180,
    )

    # move towards 2 (backwards)
    base.run_target(
        1500,
        1500,
        -1000,
        -1000,
    )

    # turn towards 3
    base.run_target(
        1500,
        1500,
        -180,
        180,
    )

    # line track from 2 to 3
    LineTrack.track(
        1500,
        [
            ((BLACK_RGB_LEFT[0] + WHITE_RGB_LEFT[0]) / 2),
            ((BLACK_RGB_LEFT[0] + WHITE_RGB_LEFT[0]) / 2),
            ((BLACK_RGB_LEFT[0] + WHITE_RGB_LEFT[0]) / 2),
        ],
        [
            ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
            ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
            ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
        ],
        see_line(3),
    )

    base.brake()
    wait(500)

    # line track from 3 to 0 (backwards)
    LineTrack.track(
        1500,
        [
            ((BLACK_RGB_LEFT[0] + WHITE_RGB_LEFT[0]) / 2),
            ((BLACK_RGB_LEFT[0] + WHITE_RGB_LEFT[0]) / 2),
            ((BLACK_RGB_LEFT[0] + WHITE_RGB_LEFT[0]) / 2),
        ],
        [
            ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
            ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
            ((BLACK_RGB_RIGHT[0] + WHITE_RGB_RIGHT[0]) / 2),
        ],
        see_line(2, left_cs_b, right_cs_b),
        left_cs_b,
        right_cs_b,
    )

    base.brake()

    #turn to face 1
    base.run_target(
        1500,
        1500,
        0,
        -360,
    )
