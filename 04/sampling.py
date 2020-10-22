import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import timeit

def sample_normal_distribution(mean, std_dev):
	samples = np.random.uniform(-std_dev, std_dev, 12)
	# print(samples)
	return mean + np.sum(samples)/2

def rejection_sampling(mean, std_dev):
	max_f = norm(mean, std_dev).pdf(mean)

	while True:
		x = np.random.uniform(-std_dev, std_dev, 1)
		y = np.random.uniform(0, max_f, 1)
		if y <= norm(mean, std_dev).pdf(x):
			break
	return x[0]

def box_muller_sampling(mean, std_dev):
	u = np.random.uniform(0,1,2)
	x = math.cos(2*np.pi*u[0]) * math.sqrt(-2*math.log(u[1]))
	return mean + std_dev*x

if __name__ == "__main__":
	# print(sample_normal_distribution(0.5, 10))
	print(rejection_sampling(5, 2.5))