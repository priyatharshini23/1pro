p=int(input())
q=input().split()
ss=[]
for i in range(p):
    r=q[i]
    for j in range(i+1,p):
        if(int(q[i])<int(q[j]))and (int(q[j-1])<int(q[j])):
            r+=q[j]
        else:
            break
    ss.append(len(r))
print(max(ss))
