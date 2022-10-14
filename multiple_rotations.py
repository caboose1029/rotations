from symtable import Symbol
from sympy.vector import CoordSys3D
from sympy import *


E = CoordSys3D('E')
theta = Symbol('theta')
psi = Symbol('psi')

A = E.orient_new_axis('A', psi, E.j)
B = A.orient_new_axis('B', theta, A.i)

rot_mat = B.rotation_matrix(E)
rot_mat = rot_mat.transpose()

q = B.quaternion(E)

pprint(rot_mat)
