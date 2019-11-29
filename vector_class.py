import numpy as np 
import matplotlib.pyplot as plt 

class vect:
	def __init__(self, *components):
		self.components = components
		self.dimensions = len(components)

	def __repr__(self):
		return("{}".format(self.components))

	def dot(self, other):
		assert self.dimensions == other.dimensions
		tot = 0
		for i, j in zip(self.components, other.components):
			tot += i*j
		return tot

	def cross(self, other):
		assert self.dimensions == other.dimensions and self.dimensions == 3
		x_self, y_self, z_self = self.components
		x_other, y_other, z_other = other.components
		x_new = y_self*z_other - z_self*y_other
		y_new = z_self*x_other - x_self*z_other
		z_new = x_self*y_other - y_self*x_other
		return vect(x_new, y_new, z_new)

v1 = vect(1, 2, 3)
v2 = vect(2, 3, 4)

print(v1.dot(v2))
print(v1.cross(v2))
print((v1.cross(v2)).dot(v1))