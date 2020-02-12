k=list(map(int,input().split()))


s=[]
for j in k:
	if j not in s:
		s.append(j)
print(*s,sep="*")

