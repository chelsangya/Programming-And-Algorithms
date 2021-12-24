#print a specified list after removing the fourth element
list=[13,23,32,59,7,32,80]
for i in list:
    if i==list[3]:
        continue
    print(i,end=" ")