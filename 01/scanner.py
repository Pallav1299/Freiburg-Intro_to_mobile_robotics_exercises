import math
import numpy as np
import matplotlib.pyplot as plt

scan = np.loadtxt("/home/pallavbhalla/Documents/Intro to mobile robotics/exercises_&_resources/01/laserscan.dat")
angle = np.linspace(-np.pi/2, np.pi/2, scan.shape[0], endpoint="true")

x = scan * np.cos(angle)
y = scan * np.sin(angle) 

Trw = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4), 1], [np.sin(np.pi/4), np.cos(np.pi/4), 0.5], [0, 0, 1]])
Tlr = np.array([[np.cos(np.pi), -np.sin(np.pi), 0.2], [np.sin(np.pi), np.cos(np.pi), 0], [0, 0, 1]])

w = np.ones(len(y))

scan_data = np.array([x, y, w])
# scan -->> Tdl

data = np.dot(np.dot(Trw, Tlr),scan_data)

plt.figure()

plt.plot(data[0,:], data[1,:], ".k", markersize=3)
# Plot robot pose in blue
plt.plot(Trw[0,2], Trw[1,2], "+b");
# Plot laser pose in red
plt.plot(np.dot(Trw, Tlr)[0,2], np.dot(Trw, Tlr)[1,2], "+r");
# plt.plot(x, y, ".k")
plt.gca().set_aspect("equal", adjustable="box")
plt.show()