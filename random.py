a=[1,2,3,4]
b=[5,7,3,0]
i=0
while i<len(a):
    j=0
    while j<len(b):
        if b[j] not in a:
            a.append(b[j])
        j+=1
    i+=1
print(a)