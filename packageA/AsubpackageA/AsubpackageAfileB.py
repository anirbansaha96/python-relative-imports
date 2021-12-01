# Import item from AsubpackageA (this file) in packageA
# Import item from AsubpackageA (this file) in packageC


from packageA.pkgAfileB import print__Name__

class MNOP:
    def __init__(self):
        print("MNOP")
        print('Class imported from : ')
        print__Name__(__name__)