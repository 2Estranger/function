# a=[1,[2,3],4,[6,[7,8],9],10]
# i=0
# n=[]
# while i<len(a):
#     if a[i]==[]:
#         continue
#     i+=1
    
a=[1,[2,3],4,[6,[7,8],9],10]
i=0
n=[]
while i<len(a):
	if type(a[i])==type([]):
		if len(a[i])>1:
			j=0
			m=len(a[i])
			while j<m:
				n.append(a[i][j])
				j=j+1
			i+=1
	else:
		n.append(a[i])
		i+=1
print(n)
# i=0
# l=[]
# m=[]
# while i<len(n):
# 	k=1
# 	c=0
# 	while k<=n[i]:
# 		if n[i]%k==0:
# 			c=c+1
# 		k=k+1
# 		b=n[i]
# 	if c==2:
# 		l.append(b)
# 	else:
# 		m.append(b)
# 	i=i+1
# print(l ,"prime") 
# print(m,"not prime")