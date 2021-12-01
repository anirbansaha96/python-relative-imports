# Import item from packageC in AsubpackageA (this file)

import os
print(os.getcwd())
try:
    print('--------------------------------------------------------')
    from packageC.pkgCfileB import WXYZ
    wxyz = WXYZ()
    print(type(wxyz))
except Exception as e:
    print(e)


try:
    print('--------------------------------------------------------')
    from ...packageC.pkgCfileB import WXYZ
    wxyz = WXYZ()
    print(type(wxyz))
except Exception as e:
    print(e)