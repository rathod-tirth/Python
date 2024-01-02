# Python

- ### Namespace :

   - Namespaces provide separate environments for names, allowing different parts of your code to have their own set of names without conflicting with each other. 

   - Even if two namespaces have names that are identical, they refer to different things within their respective environments, keeping the code organized and preventing conflicts.

   - A namespace is also called context or scope.

   - The built-in function `dir()` returns a list of defined names in a namespace.

## Packages and Modules :

- Packages and modules are essential for code organization, reusability, and maintaining clean and scalable Python projects. They allow you to encapsulate functionality, reduce naming conflicts, and structure code logically.

- There are in-built modules like math, random, etc.

- ### Modules :

   - A module in Python is simply a file containing Python code. It can define functions, classes, and variables. 
   
   - Any Python file can be imported as a module in another Python script, allowing you to reuse code.

   ```python
   import mod # importing module
   
   from mod import func() # individual object
   
   from mod import func(), data # multiple objects
   
   from mod import * # everything
   
   from mod import data as name # alias names for object
   
   import mod as school # alias names for module

   ```

   - Python 3 does not allow import * within a function

   ```python
   def fun():
      from mod import *

   # SyntaxError: import * only allowed at module level
   ```

- ### Packages :

   - A package is a collection of Python modules. It's a way to organize modules into hierarchical directories and sub-directories. 
   
   ```python
   import pack.mod # importing module from a package

   from pack.mod import fun() # object from a package

   # etc is also same just need to refer the package using dot notation
   ```
   
   - A package contains an `__init__.py` file (which can be empty) to indicate that the directory should be treated as a package.

   - It is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code.

   - You can import all the modules by importing the package, this could be achieved by importing all the modules in init file prior. 

   - `__name__` refers to the package name it belongs to.

   - `__all__` can be used to manipulate the `*` functionality. In packages without `__all__` nothing is imported and in modules everything is imported while using `*`. You can speficy what to import when using `*` in `__all__` file.

   ```python
   # init.py

   a=["good","nice","happy"]

   print(f"Name of the package : {__name__}")

   import mod1,mod2,mod3 # only need to import Package and all the module inside it will be imported

   __all__=["mod1","mod2"]
   
   ```

   - **Note :** From Python 3.3, Implicit Namespace Packages were introduced. These allow for the creation of a package without any` __init__.py` file.

