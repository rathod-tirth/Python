# Python

### Namespace :

   - Namespaces provide separate environments for names, allowing different parts of your code to have their own set of names without conflicting with each other. 

   - Even if two namespaces have names that are identical, they refer to different things within their respective environments, keeping the code organized and preventing conflicts.

   - A namespace is also called context or scope.

   - The built-in function `dir()` returns a list of defined names in a namespace.

## Packages and Modules :

- Packages and modules are essential for code organization, reusability, and maintaining clean and scalable Python projects. They allow you to encapsulate functionality, reduce naming conflicts, and structure code logically.

- There are in-built modules like math, random, etc.

### Modules :

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

### Packages :

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

## File Handling :

- File handling is a process of working with files ,which involves creating, reading, writing, updating, and deleting the files.

- Python supports file handling i.e., to read, write, append with many other handling options to operate on files.

### Open : 

   - The `open()` function basically opens the file. Before performing any operation on the file like reading or writing first, we need to open the file.

   - Python provides `open()` function to open the file which takes 2 arguments : 1. filename 2. in which mode you want to open the file.

   ```python
   f = open('filename.txt','mode')

   f.close()
   ```

- **Close :** Remember to close the file you have opened using the `close()`, this will prevent data leakage and corruption.

### Read :

   - While opening the file you can pass 'r' in the second argument, this will open the file in read mode.

   - Read mode only allows to read the file and no other operations.

   ```python
   file = open('filename.txt','r')
   file.close()
   ```

   - If the file doesn't exist it will throw an error.

   - Python uses pointer to keep track of current position inside the file.

   - The pointer remembers the current position and determines from where the next read operation will start.

   - The pointer advances automatically through the content, allowing you to access the data sequence wise and subsequent read operations will start from where the previous one ended.

   - Functions :

      - `read()` : retuns entire file as string

      - `readlines()` : returns each line as a list element

      - `realine()` : returns single line as string

      - `readable()` : returns boolean values if the file is readable or not

      ```python
      # read()
      file=open('filename.txt','r')
      
      read=file.read()
      file.close()
      ```

      - Each of the in-built functions can take one argument, which tells the pointer how far does it has to travel and that will be the returning statement.

### Write :

- Pass 'w' in the second argument while opening a file, this will open the file in write mode.

- If the file doesn't exist it will create one.

```python
file=open('filename.txt','w')
file.close()
```

- Functions :

   - `write()` : to write string in the file

   - `writelines(iterator)` : to write multiple lines of string in the file, it takes an iterator (list, tuple, dict) as an argument

   - `writable()` : returns boolean values if the file is writeable or not

   ```python
   file=open('filename.txt','w')
   
   file.write("Hello")
   file.close()
   ```

- Write mode overides the existing data. So if you reopen the file and write something else the existing data will be gone only the new data will be there.

- Multiple write function on an open file will increment the data and won't overwrite each other.

```python
# ----- Will overwrite -------
file=open('filename.txt','w')
file.write("Hello")
file.close()

file=open('filename.txt','w')
file.write("Hi")
file.close()
# ---------------------------

# ------ Won't overwrite -------
file=open('filename.txt','w')
file.write("Hello")
file.write("How are you doing?")
file.close()
# -------------------------
```

### Append :

- Pass 'a' in the second argument while opening a file, this will open the file in append mode.

- Append mode doesn't overwrite the existing data. It adds new data to the existing data.

- If the file doesn't exist it will create a new one.

- Use the same functions of write mode to write the data.

```python
file=open('filename.txt','a')
file.write("Hello")
file.close()
```

### Other Modes :

- '+' in second argument combines two mode and is helpful when there is more than one operations.

- 'r+' for read and write operation on file.

- 'w+' for write and append operation on file.

- 'a+' for append and read operation on file.

- 'b' opens the file in binary mode.

- 'x' opens the file for exclusive creation. If the file already exists it will throw an error.

### With :

- It is very commom mistake to forget to close the file, which causes data leakage and corruption.

- Here we can use with statement, which automatically close the file once the code is executed and prevents data leakage and corruption.

- It also runs the code inside its own code block which makes the code more organised.

```python
with open('filename','mode') as file:
   print(file.read())
   # other operations...

# no need to close the file it will automatically closes the file
```

### Seek :

- To control the pointer inside the file we can use `seek()` function, which places the pointer at the desired position.

```python
file=open('filename','r')

file.read() # returns the entire file

file.seek(0) # position the pointer at start

file.read() # also returns the entire file

file.close()
```