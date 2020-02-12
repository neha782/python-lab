l1=[1,3,4,2]
l2=[1,4,9,5]
l=[l1.append(i) for i in l2 if i not in l1]
print(l1)
