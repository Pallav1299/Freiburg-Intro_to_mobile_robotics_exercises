import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def gaussian_noise(sigma):
    return (1/(np.sqrt(2*np.pi)*sigma))*np.exp((-(z-zexp)**2)/(2*sigma))

def distance(p1, p2):
    return np.sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)

def likelihood(m):
    x0 = np.array([12,4])
    x1 = np.array([5,7])

    d0 = 3.9
    d1 = 4.5
    var0 = 1
    var1 = 1.5

    d0_ = distance(m, x0)
    d1_ = distance(m, x1)

    pdf0 = norm.pdf(d0, d0_, var0)
    pdf1 = norm.pdf(d1, d1_, var1)

    return pdf0*pdf1


if __name__ == "__main__":
    m0 = np.array([10,8])
    m1 = np.array([6,3])
    x0 = np.array([12,4])
    x1 = np.array([5,7])
    
    x = np.arange(3.0,15.0,0.5)
    y = np.arange(-5.0,15.0,0.5)
    X,Y = np.meshgrid(x,y)

    z = np.array([likelihood(np.array([x,y])) for x,y in zip(X.flatten(), Y.flatten())])
    Z = z.reshape(X.shape)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.coolwarm,alpha=0.5)

    ax.scatter(m0[0],m0[1],likelihood(m0),c="g",marker="o",s=100)
    ax.scatter(m1[0],m1[1],likelihood(m1),c="r",marker="o",s=100)
    ax.scatter(x0[0],x0[1],likelihood(x0),c="g",marker="^",s=100)
    ax.scatter(x1[0],x1[1],likelihood(x1),c="r",marker="^",s=100)
    ax.set_xlabel("m_x")
    ax.set_ylabel("m_y")
    ax.set_zlabel("likelihood")
    plt.show()