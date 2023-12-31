'''
    List methods     

        >> to add element
        
        1) list.append(element) : insert element at end of the list

        2) list.insert(pos,element) : insert element at specific position

        3) list.extend([list]) : merges list at the end
 
        >> to remove element

        1) list.pop() : remove last element
            ilst.pop(index) : will remove from index

        2) list.remove(elemennt) : will remove based on element itself

        3) list.clear() : will blank the whole list

        4) del keyword : deletes the element

        >> other

        1) sort : 
            - sorts list in ascending or descending order
            - list.sort(key=..., reverse=...)
            - sorts the original list

        2) reverse : reverse the list

        3) count : count the duplication of element
'''

li=[21,"Hello",77,92,"have",'a',3,6.5,"gg",105,42,77,'a']

print("original list :",li)

# --append--

li.append("day")
print("append :",li)

# --insert--

li.insert(5,69)
print("insert :",li)

# --extend--

li1=["welcome",31]

li.extend(li1)
print("extend :",li)

# --pop--

li.pop()
li.pop(11)
print("pop :",li)

# --remove--

li.remove("welcome")
print("remove :",li)


# --reverse--

li.reverse()
print(li)

# --count--

print("77 in list:",li.count(77))

# --sort--

li2=[55,78,92,13,5,102,66,18]
# ascending order

li2.sort()
print(li2)

# descending order
li2.sort(reverse=True)
print(li2)

# --del--

del li[10]
print("delete :",li)
# del li #used for deleting the variable

# --clear--

li.clear()
print("clear :",li)













