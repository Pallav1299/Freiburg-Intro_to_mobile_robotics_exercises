import numpy as np
import matplotlib.pyplot as pyt 

def diff_drive(x, y, theta, v_l, v_r, t, l):

	if v_l==v_r:
		x_n = x + v_r*t*(np.cos(theta))
		y_n = y + v_r*t*(np.sin(theta))
		theta_n = theta

	else:
		R = (l/2)*((v_r + v_l)/(v_r - v_l))

		centre_x = x - R*np.sin(theta)
		centre_y = y + R*np.cos(theta)

		w = (v_r - v_l)/l
		d_theta = w*t
		theta_n = theta + d_theta

		x_n = (x - centre_x)*np.cos(d_theta) - (y - centre_y)*np.sin(d_theta) + centre_x
		y_n = (x - centre_x)*np.sin(d_theta) - (y - centre_y)*np.cos(d_theta) + centre_y

	return x_n, y_n, theta_n

def main():
	(x , y, theta) = (1.5, 2, np.pi/2)
	print(x, y, theta)
	x, y, theta = diff_drive(x, y, theta, 0.3, 0.3, 3, 0.5)
	print(x, y, theta)
	x, y, theta = diff_drive(x, y, theta, 0.1, -0.1, 1, 0.5)
	print(x, y, theta)
	x, y, theta = diff_drive(x, y, theta, 0.2, 0, 2, 0.5)
	print(x, y, theta)

if __name__ == "__main__":
	main()