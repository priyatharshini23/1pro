p=int(input())
q=2**p
z=[]
for i in range(0,q):
    l=bin(i)[2:].zfill(p)
    if(len(l)<len(bin(2**p-1)[2:])):
        z.append([l.count("1"),l])
    else:
        z.append([l.count("1"),l])
z.sort()
for i in range(len(z)):
    print(z[i][1])
