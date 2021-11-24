import os
try:
    from packageA.pkgAfileA import ABCD
    # from packageA.pkgAfileB import printCWD, print__Name__
    abcd = ABCD()
    print(type(abcd))
    # printCWD(os.getcwd())
    # print__Name__(__name__)
except Exception as e:
    print(e)
    print("Error: unable to import packageA.pkgAfileA")

try:
    from ..packageA.pkgAfileA import ABCD
    # from ..packageA.pkgAfileB import printCWD, print__Name__
    abcd = ABCD()
    print(type(abcd))
    # printCWD(os.getcwd())
    # print__Name__(__name__)
except Exception as e:
    print(e)
    print("Error: unable to import ..packageA.pkgAfileA")
