import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
A class for vector fields.
"""

class vec_field:
	def __init__(self, *f):
		#f is a set of lambda functions representing the components of the vector field
		self.components = f
		self.dimensions = len(f)

	def get_vec(self, *coords):
		#Get the vector at a particular coordinate
		assert len(coords) == self.dimensions
		v_res = []
		for func in self.components:
			v_res.append(func(*coords))
		return np.array(v_res)

	def get_partial_diffs(self, *coords):
		#Obtain values of partial differentials at a coordinate
		#Change n to vary accuracy
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
		return np.array(partials)

	def get_divergence(self, *coords):
		#Obtain divergence at a coordinate
		assert len(coords) == self.dimensions
		div = 0
		partials = self.get_partial_diffs(*coords)
		for i in range(len(coords)):
			div += partials[i][i]
		return div

	def get_curl(self, *coords):
		#Get curl for 2D or 3D vectors
		assert len(coords) in [2, 3] and len(coords) == self.dimensions
		if len(coords) == 2:
			partials = self.get_partial_diffs(*coords)
			return np.array([partials[0][1] - partials[1][0]])
		else:
			partials = self.get_partial_diffs(*coords)
			return np.array([partials[1][2] - partials[2][1], partials[2][0] - partials[0][2], partials[0][1] - partials [1][0]])

	def plot_field2D(self, **kwargs):
		#Plot color coded 2D vector fields
		#xlim and ylim are boundaries for the plot (list of 2 elements each)
		#Set frequency to change frequency of vectors
		assert self.dimensions == 2
		freq = 20
		xlim = [-10, 10]
		ylim = [-10, 10]
		for key, value in kwargs.items():
			assert key in ["freq", "xlim", "ylim"]
			if key == "freq":
				freq = value
			elif key == "xlim":
				xlim = value
			else:
				ylim = value
		x = np.linspace(xlim[0], xlim[1], freq)
		y = np.linspace(ylim[0], ylim[1], freq)
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

	def plot_field3D(self, **kwargs):
		#Plot 3D vector fields
		#xlim, ylim and zlim are boundaries for the plot
		#Set frequency to change frequency of vectors
		#Note that vectors ONLY show directions. As of now color coding 3D plots are beyond my calibre
		assert self.dimensions == 3
		freq = 20
		xlim = [-10, 10]
		ylim = [-10, 10]
		zlim = [-10, 10]
		lw = 0.5
		for key, value in kwargs.items():
			assert key in ["freq", "xlim", "ylim", "zlim", "lw"]
			if key == "freq":
				freq = value
			elif key == "xlim":
				xlim = value
			elif key == "ylim":
				ylim = value
			elif key == "zlim":
				zlim = value
			else:
				lw = value
		x = np.linspace(xlim[0], xlim[1], freq)
		y = np.linspace(ylim[0], ylim[1], freq)
		z = np.linspace(zlim[0], zlim[1], freq)
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
		ax.quiver(X, Y, Z, U, V, W, lw = lw)
		plt.show()

fx2D = lambda x, y : x + y
fy2D = lambda x, y : x**2 + 2*y

fx3D = lambda x, y, z : x*y + 2*x*z
fy3D = lambda x, y, z : z*x**2 + 2*y*z
fz3D = lambda x, y, z : x**3 + 2*(x**2)*(y**2)*z

field2D = vec_field(fx2D, fy2D)
field3D = vec_field(fx3D, fy3D, fz3D)

x, y, z = (2, 3, 1)

print("Field1: [x + y, x**2 + 2*y]")
print("Field1 dimensions: {}".format(field2D.dimensions))
print("Field1 vector at ({}, {}): {}".format(x, y, field2D.get_vec(x, y)))
print("Field1 partial derivatives at ({}, {}): {}".format(x, y, field2D.get_partial_diffs(x, y)))
print("Field1 divergence at ({}, {}): {}".format(x, y, field2D.get_divergence(x, y)))
print("Field1 curl at ({}, {}): {}".format(x, y, field2D.get_curl(x, y)))
field2D.plot_field2D(xlim = [-10, 10], ylim = [-10, 10], freq = 20)

print("\n")
print("Field2: [x*y + 2*x*z, z*x**2 + 2*y*z, x**3 + 2*(x**2)*(y**2)*z]")
print("Field2 dimensions: {}".format(field3D.dimensions))
print("Field2 vector at ({}, {}, {}): {}".format(x, y, z, field3D.get_vec(x, y, z)))
print("Field2 partial derivatives at ({}, {}, {}): {}".format(x, y, z, field3D.get_partial_diffs(2, 3, 1)))
print("Field2 divergence at ({}, {}, {}): {}".format(x, y, z, field3D.get_divergence(2, 3, 1)))
print("Field2 curl at ({}, {}, {}): {}".format(x, y, z, field3D.get_curl(2, 3, 1)))
field3D.plot_field3D(xlim = [-10, 10], ylim = [-10, 10], zlim = [-10, 10], freq = 10, lw = 0.5)