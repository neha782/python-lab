l=[]
while 1:
	item =input("enter the item")
	l=l+[item]
	n=input("do you want to continue Y/N")
	if n.lower()=='n':
		break
print(l)
l.sort(reverse=True,key=len)
print(l)
l.sort(reverse=True,key=max)
print(l)


		
