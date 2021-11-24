import os
try:
    print('-------------------------------------------------------------')
    from packageA.pkgAfileA import ABCD
    from packageA.pkgAfileB import printCWD, print__Name__
    printCWD(os.getcwd())
    abcd = ABCD()
    print(type(abcd))
    print__Name__(__name__)
except Exception as e:
    print(e)

try:    
    print('-------------------------------------------------------------')
    from packageA.pkgAfileA import ABCD
    from packageA import pkgAfileB    
    printCWD(os.getcwd())
    abcd = ABCD()
    print(type(abcd))
    pkgAfileB.printCWD(os.getcwd())
    pkgAfileB.print__Name__(__name__)
except Exception as e:
    print(e)

try:
    print('-------------------------------------------------------------')
    from .packageA.pkgAfileA import ABCD
    from .packageA.pkgAfileB import printCWD, print__Name__  
    printCWD(os.getcwd())
    abcd = ABCD()
    print(type(abcd))
    pkgAfileB.printCWD(os.getcwd())
    pkgAfileB.print__Name__(__name__)
except Exception as e:
    print(e)

try:
    print('-------------------------------------------------------------')
    from .packageA.pkgAfileA import ABCD
    from .packageA import pkgAfileB
    printCWD(os.getcwd())
    abcd = ABCD()
    print(type(abcd))
    pkgAfileB.printCWD(os.getcwd())
    pkgAfileB.print__Name__(__name__)
except Exception as e:
    print(e)