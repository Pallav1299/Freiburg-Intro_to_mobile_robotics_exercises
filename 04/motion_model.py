#!/usr/bin/env python
"""
* Date    		: 2020-09-17 17:35:07
* Author  		: Pallav Bhalla (pallav.bhalla@fluxauto.xyz)
* Link   		: https://github.com/pallav1299
* Version 		: 1.0.0
* Description	: 
"""

import numpy as np
import matplotlib.pyplot as plt
from sampling import sample_normal_distribution

def odometry_motion_model(u, state, a):
    """
    Arguments:
    state -- pose of the robot before moving [x, y, theta]
    u -- odometry reading obtained from the robot [rot1, rot2, trans]
    a -- noise parameters of the motion model [a1, a2, a3, a4]
    """

    delta_r1 = u[0] + sample_normal_distribution(0, a[0]*abs(u[0]) + a[1]*abs(u[2]))
    delta_r2 = u[1] + sample_normal_distribution(0, a[0]*abs(u[1]) + a[1]*abs(u[2]))
    delta_trans = u[2] + sample_normal_distribution(0, a[2]*abs(u[2]) + a[3]*(abs(u[0])+abs(u[1])))

    x = state[0] + delta_trans*np.cos(state[2] + delta_r1)
    y = state[1] + delta_trans*np.sin(state[2] + delta_r1)
    theta = state[2] + delta_r1 + delta_r2
    return [x, y, theta]

def eval_motion_model(u, state, a):
    pose_x = []
    pose_y = []
    for i in range(5000):
        tmp = odometry_motion_model(u, state, a)
        pose_x.append(tmp[0])
        pose_y.append(tmp[1])
    plt.plot(state[0], state[1], "bo")
    plt.plot(pose_x, pose_y, "r,")
    # plt.xlim([1, 3])
    plt.axes().set_aspect("equal")
    plt.xlabel("x-position [m]")
    plt.ylabel("y-position [m]")
    plt.show()

if __name__ == "__main__":
    state = [0, 0, 0]
    odom = [np.pi/2, 0, 1]
    alpha = [0.1, 0.1, 0.01, 0.01]
    # print(odometry_motion_model(odom, state, alpha))
    eval_motion_model(odom, state, alpha)