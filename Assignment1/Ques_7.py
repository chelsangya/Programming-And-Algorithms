#add an item in a tuple
tuple1=(1,2,3,6,9,5,4)
l1=list(tuple1)
l1.append(0)
tuple1=tuple(l1)
print(tuple1)