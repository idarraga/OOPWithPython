"""
Define the C-variables and functions from the C-files that are needed in Python
"""
from ctypes import c_double, c_int, CDLL
import sys
import numpy as np

lib_path = 'c_interface/calc_force_%s.so' % (sys.platform)
try:
    basic_function_lib = CDLL(lib_path)
except:
    print('OS %s not recognized' % (sys.platform))

python_calc_force = basic_function_lib.calc_force
python_calc_force.restype = None

list_in = np.array([1.0, 2.0, 1.0, 2.0, 1.0, 1.0])
n = len(list_in)

c_arr_in = (c_double * n)(*list_in)
c_arr_out = (c_double * n)()

python_calc_force(c_arr_in, c_double(1.0), c_arr_out)

print("Test ! %s %s"%(c_arr_out[0], c_arr_out[1]))
