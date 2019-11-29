import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class vec_field:
	def __init__(self, *f):
		#f is a set of lambda functions representing the components of the vector field
		self.components = f
		self.dimensions = len(f)

	def get_vec(self, *coords):
		assert len(coords) == self.dimensions
		v_res = []
		for func in self.components:
			v_res.append(func(*coords))
		return v_res

	def get_partial_diffs(self, *coords):
		assert len(coords) == self.dimensions
		partials = []
		v_res = self.get_vec(*coords)
		coords = list(coords)
		for i in range(len(coords)):
			n = 7
			di = 10**(-n)
			coords[i] += di
			v_temp = self.get_vec(*coords)
			v_par = [round((j - i)/di, n-2) for i, j in zip(v_res, v_temp)]
			coords[i] -= di
			partials.append(v_par)
		return partials

	def get_divergence(self, *coords):
		assert len(coords) == self.dimensions
		div = 0
		partials = self.get_partial_diffs(*coords)
		for i in range(len(coords)):
			div += partials[i][i]
		return div

	def get_curl2D(self, *coords):
		assert len(coords) == 2 and len(coords) == self.dimensions
		partials = self.get_partial_diffs(*coords)
		return [partials[0][1] - partials[1][0]]

	def get_curl3D(self, *coords):
		assert len(coords) == 3 and len(coords) == self.dimensions
		partials = self.get_partial_diffs(*coords)
		return [[partials[1][2] - partials[2][1]], [partials[2][0] - partials[0][2]], [partials[0][1] - partials [1][0]]]

	def plot_field2D(self, xlim, ylim):
		assert self.dimensions == 2
		step = 1
		x = np.arange(xlim[0], xlim[1], step)
		y = np.arange(ylim[0], ylim[1], step)
		X, Y = np.meshgrid(x, y)
		U = self.components[0](X, Y)
		V = self.components[1](X, Y)
		colors = np.sqrt(U**2 + V**2)
		U = U/colors
		V = V/colors
		fig = plt.figure()
		ax = plt.gca()
		ax.quiver(X, Y, U, V, colors, scale_units = "xy", angles = "xy")
		plt.show()

	def plot_field3D(self, xlim, ylim, zlim):
		assert self.dimensions == 3
		step = 2
		x = np.arange(xlim[0], xlim[1], step)
		y = np.arange(ylim[0], ylim[1], step)
		z = np.arange(zlim[0], zlim[1], step)
		X, Y, Z = np.meshgrid(x, y, z)
		U = self.components[0](X, Y, Z)
		V = self.components[1](X, Y, Z)
		W = self.components[2](X, Y, Z)
		colors = np.sqrt(U**2 + V**2 + W**2)
		U = U/colors
		V = V/colors
		W = W/colors
		fig = plt.figure()
		ax = plt.gca(projection = "3d")
		ax.quiver(X, Y, Z, U, V, W, lw = 0.5)
		plt.show()

fx2D = lambda x, y : x + y
fy2D = lambda x, y : x**2 + 2*y

fx3D = lambda x, y, z : x*y + 2*x*z
fy3D = lambda x, y, z : z*x**2 + 2*y*z
fz3D = lambda x, y, z : x**3 + 2*(x**2)*(y**2)*z

field2D = vec_field(fx2D, fy2D)
field3D = vec_field(fx3D, fy3D, fz3D)

print(field2D.get_vec(2, 3))
print(field2D.get_partial_diffs(2, 3))
print(field2D.get_divergence(2, 3))
print(field2D.get_curl2D(2, 3))
field2D.plot_field2D([-10, 10], [-10, 10])

print(field3D.get_vec(2, 3, 1))
print(field3D.get_partial_diffs(2, 3, 1))
print(field3D.get_divergence(2, 3, 1))
print(field3D.get_curl3D(2, 3, 1))
field3D.plot_field3D([-10, 10], [-10, 10], [-10, 10])