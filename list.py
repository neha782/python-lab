l=[]
while 1:
	item =input("enter the item")
	l+=[item]
	n=input("do tri maa ki you want to continue Y/N")
	if n.lower()=='n':
		break
print(l)
l.sort(reverse=True,key=len)
print(l)
l.sort(reverse=True,key=max)
print(l)


		
