import numpy as np
import matplotlib.pyplot as plt

def custom(x):
	return np.cos(x)*np.exp(x)

def customCall():
	x = np.linspace(-2*np.pi, 2*np.pi, 100, endpoint=False)
	plt.plot(x,custom(x))
	plt.xlabel("x")
	plt.ylabel("cos(x)*exp(x)")
	# plt.show()
	plt.savefig("00_result.png")

def generateNormal(mu, sigma, n):
	return np.random.normal(mu, sigma, n)

def generateNormalCall():
	mu, sigma, n = 5, 2, 100000
	s = generateRandom(mu, sigma, n)
	count, bins, ignored = plt.hist(s, 1000, density=True)
	# plt.plot(bins)
	plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
	plt.show()

def generateUniform(start, end, n):
	return np.random.uniform(start, end, n)

def generateUniformCall():
	u = generateUniform(0, 10, 100000)
	count, bins, ignored = plt.hist(u, 10000, normed=True)
	plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
	plt.show()

def findStdDev(x):
	return np.sqrt(np.sum((x-np.mean(x))**2)/(len(x)-1))

def findMean(x):
	return np.mean(x)

def main():
	u = generateUniform(0, 10, 100000)
	x = np.linspace(-2*np.pi, 2*np.pi, 100, endpoint=False)
	print(findStdDev(u))
	

if __name__=="__main__":
	main()