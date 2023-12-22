'''

    >> map() function returns a map object(which is an iterator) of the results after applying the given function
       to each item of a given iterable

    >> Syntax: map(fun, iter)

    >> Parameters:

        - fun: It is a function to which map passes each element of given iterable.
        - iter: It is iterable which is to be mapped.

    Returns: Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

    >> NOTE :
    
        - The returned value from map() (map object) then can be passed to functions like list(), set().
        - You can pass one or more iterable to the map() function.

'''

# map with function

li=[5,10,15,26,34,50]

def sqr(x):
    return x*x

sqr_li=list(map(sqr,li))

print(f"{li}\nSquare of list: {sqr_li}\n\n")

# map with lambda function

li2=[3,5,8,16,20]

cube_li=list(map(lambda x: x*x*x, li2))

print(f"{li2}\nCube of list: {cube_li}\n\n")

# adding to list with map function

li3=[5,10,6,9,12]
li4=[5,2,4,15,20]

add_li=list(map(lambda x,y:x+y, li3,li4))

print(f"{li3}\n{li4}\nAddition of above list: {add_li}")








