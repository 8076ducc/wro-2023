#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Color, Button
from pybricks.tools import wait
from devices import *
from pid import *
from constants import *

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
        lambda: (left_cs_f.rgb()[0] > BLACK_RGB_LEFT[0] + 5 and right_cs_f.rgb()[0] > BLACK_RGB_RIGHT[0] + 5),
    )

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
        lambda: (left_cs_f.rgb()[0] > BLACK_RGB_LEFT[0] + 5 and right_cs_f.rgb()[0] > BLACK_RGB_RIGHT[0] + 5),
    )

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
        lambda: (left_cs_b.rgb()[0] > BLACK_RGB_LEFT[0] + 5 and right_cs_b.rgb()[0] > BLACK_RGB_RIGHT[0] + 5),
        left_cs_b,
        right_cs_b,
    )

    #turn to face 1
    base.run_target(
        1500,
        1500,
        360,
        -360,
    )
