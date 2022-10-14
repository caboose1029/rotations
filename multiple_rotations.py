from symtable import Symbol
from sympy.vector import CoordSys3D
from sympy import *


E = CoordSys3D('E')
theta = Symbol('theta')
phi = Symbol('phi')
psi = Symbol('psi')

A = E.orient_new_axis('A', theta, E.i)
B = A.orient_new_axis('B', phi, A.j)
C = B.orient_new_axis('C', psi, B.j)

rot_mat = C.rotation_matrix(E)
rot_mat = rot_mat.transpose()

pprint(rot_mat)
