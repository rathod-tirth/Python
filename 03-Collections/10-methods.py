'''
>> Methods used in all types of iterable
   
>> Sorted
   - sorted(list, key=..., reverse=...)
   - returns a new sorted list
   
>> Difference Between Sort and Sorted:
   - sort : sorts the original list
   - sorted : returns a new sorted list
'''

# --sorted--
li1=[55,78,92,13,5,102,66,18]
tup1=(5,10,35,87,12,65,101)
di1={5:"hello",56:"nice",84:"good",23:"fine"}

sort_li=sorted(li1)
sort_tup=tuple(sorted(tup1))
sort_di=dict(sorted(di1.items()))

print("List :",sort_li)
print("Tuple :",sort_tup)
print("Dict :",sort_di)
