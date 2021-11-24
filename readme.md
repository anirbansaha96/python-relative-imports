The intention of this mini-project is to emphasize on how Relative Imports work in Python.

The best solution I found while trying to search for the answer was by BrenBarn in stackoverflow : https://stackoverflow.com/a/14132912/14384792

** Highlights / TL;DR **

1. There is a big difference between directly running a Python file, and importing that file from somewhere else. Just knowing what directory a file is in does not determine what package Python thinks it is in. That depends, additionally, on how you load the file into Python (by running or by importing).

2. There are two ways to load a Python file: as the top-level script, or as a module. 

Some Differences:

|                                        Property                                        |                       Top-level Script                      |                                                 Module                                                |                                                   Explanation (if any required)                                                   |
|:--------------------------------------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------:|
|                                   How it is executed                                   | Executed Directly - `python myfile.py` on the command line. |                        import statement is encountered inside some other file.                        |                                                                                                                                   |
| When a file is loaded, it is given a name  (which is stored in its __name__ attribute) |                           __main__                          | filename, preceded by the names of any packages/subpackages of which it is a part, separated by dots. | If we import the module pkgAfileA, its name will be packageA.pkgAfileA, but if we run pkgAfileA.py then its name will be __main__ |
|                                                                                        |                                                             |                                                                                                       |                                                                                                                                   |

3. Name of Module depends on whether it was imported directly or via a package. 
