try:
    from packageA.pkgAfileA import ABCD
    abcd = ABCD()
    print(type(abcd))
except Exception as e:
    print(e)
    print("Error: unable to import packageA.pkgAfileA")

try:
    from pkgAfileA import ABCD
    abcd = ABCD()
    print(type(abcd))
except Exception as e:
    print(e)
    print("Error: unable to import pkgAfileA")

try:
    from .pkgAfileA import ABCD
    abcd = ABCD()
    print(type(abcd))
except Exception as e:
    print(e)
    print("Error: unable to import .pkgAfileA")