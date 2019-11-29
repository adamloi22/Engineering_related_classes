import numpy as np 
import matplotlib.pyplot as plt

class Mohr2D:
	def __init__(self, sigmaxx, sigmayy, tauxy):
		self.sigmaxx = sigmaxx
		self.sigmayy = sigmayy
		self.tauxy = tauxy
		self.centre = (sigmaxx + sigmayy)/2
		self.radius = ((sigmaxx - self.centre)**2 + tauxy**2)**0.5

	def plot(self):
		theta_list = np.arange(0, 2*np.pi, 0.001)
		cart_vec = []
		r = self.radius
		for theta in theta_list:
			cart_vec.append([self.centre + r*np.cos(theta), r*np.sin(theta)])
		cart_vec = np.array(cart_vec)
		fig = plt.figure()
		ax = fig.gca()
		ax.plot(cart_vec[:, 0], cart_vec[:, 1])
		ax.plot(self.sigmaxx, self.tauxy, "o")
		ax.plot(self.sigmayy, -self.tauxy, "o")
		ax.grid()
		ax.set_xlabel("$\\sigma ($N/mm$^2)$")
		ax.set_ylabel("$\\tau ($N/mm$^2)$")
		plt.show()

	def get_principle_stresses(self):
		principle_stresses = [self.centre + self.radius, self.centre - self.radius]
		return principle_stresses

	def get_principle_directions(self):
		#principle directions: how much angle clockwise to get no shear stresses in degrees
		direction1 = 0.5*np.arctan(self.tauxy/(self.sigmaxx - self.centre))*(180/(2*np.pi))
		if direction1 > 0:
			direction2 = direction1 - 90
		if direction1 < 0:
			direction2 = direction1 + 90
		principle_directions = [direction1, direction2]
		return principle_directions

mohr = Mohr2D(10, 20, 10)
print(mohr.get_principle_stresses())
print(mohr.get_principle_directions())
mohr.plot()