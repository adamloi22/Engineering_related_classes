import numpy as np 
import matplotlib.pyplot as plt 

"""
A class for vectors.
"""

class vec:
	def __init__(self, *components):
		#components is a list of values of the vector
		self.components = components
		self.dimensions = len(components)
		mag_squared = 0
		for i in self.components:
			mag_squared += i**2
		self.magnitude = mag_squared**0.5

	def __repr__(self):
		return("{}".format(self.components))

	def __add__(self, other):
		assert self.dimensions == other.dimensions
		return [i + j for i, j in zip(self.components, other.components)]

	def __sub__(self, other):
		assert self.dimensions == other.dimensions
		return [i - j for i, j in zip(self.components, other.components)]

	def dot(self, other):
		#dot produc between any dimension of vectors
		assert self.dimensions == other.dimensions
		tot = 0
		for i, j in zip(self.components, other.components):
			tot += i * j
		return tot

	def cross(self, other):
		#cross product between 3D vectors
		assert self.dimensions == other.dimensions and self.dimensions == 3
		x_self, y_self, z_self = self.components
		x_other, y_other, z_other = other.components
		x_new = y_self*z_other - z_self*y_other
		y_new = z_self*x_other - x_self*z_other
		z_new = x_self*y_other - y_self*x_other
		return vec(x_new, y_new, z_new)

	def cart_to_cyl(self):
		#Converts cartesian coordinates to cylindrcal polar coordinates
		assert self.dimensions in [2, 3]
		quadrant = 0
		if self.components[0] > 0:
			if self.components[1] > 0:
				quadrant = 1
			elif self.components[1] < 0:
				quadrant = 4
		elif self.components[0] < 0:
			if self.components[1] > 0:
				quadrant = 2
			elif self.components[1] < 0:
				quadrant = 3
		r = self.magnitude
		theta = 0
		if quadrant in [1, 4]:
			theta = np.arctan(self.components[1]/self.components[0])
		elif quadrant == 2:
			theta = np.arctan(self.components[1]/self.components[0]) + np.pi
		elif quadrant == 3:
			theta = np.arctan(self.components[1]/self.components[0]) - np.pi
		elif quadrant == 0:
			if self.components[1] > 0:
				theta = np.pi
			elif self.components [1] < 0:
				theta = -np.pi
			elif self.components[0] >= 0:
				theta = 0
			elif self.components[0] < 0:
				theta = 2*np.pi
		if self.dimensions == 2:
			return [r, theta]
		else:
			return [r, theta, self.components[2]]

v1 = vec(-1, 2, 3)
v2 = vec(2, 3, 4)

print(v1)
print(v1 + v2)
print(v1 - v2)
print(v1.dot(v2))
print(v1.cross(v2))
print((v1.cross(v2)).dot(v1))
print(v1.cart_to_cyl())