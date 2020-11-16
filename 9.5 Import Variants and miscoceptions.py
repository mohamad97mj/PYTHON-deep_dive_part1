import sys
# from math import sqrt
# not more efficient
# in both case the math module should load in the memory

# from cmath import *
# from math import *

# sqrt will be the second
from cmath import sqrt

print('cmath' in sys.modules)
print('cmath' in globals())

import cmath

print('cmath' in globals())
