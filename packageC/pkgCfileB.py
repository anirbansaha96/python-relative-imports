# Import item from packageC (this file) in AsubpackageA 
from packageA.pkgAfileB import  print__Name__

class WXYZ:
    def __init__(self):
        print("WXYZ")
        print('Class imported from : ')
        print__Name__(__name__)