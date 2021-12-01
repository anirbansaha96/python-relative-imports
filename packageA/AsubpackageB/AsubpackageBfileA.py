# Import item from AsubpackageA in packageA (this file)

import os
print(os.getcwd())
try:
    print('--------------------------------------------------------')
    from packageA.AsubpackageA.AsubpackageAfileB import MNOP
    mnop = MNOP()
    print(type(mnop))
except Exception as e:
    print(e)


try:
    print('--------------------------------------------------------')
    from ..AsubpackageA.AsubpackageAfileB import MNOP
    mnop = MNOP()
    print(type(mnop))
except Exception as e:
    print(e)