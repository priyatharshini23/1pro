p = int(input())
q= list(map(int, input().split()))
maximum = 0
r = 0
any = q[0]
for i in range(0,p-1):
    if any < q[i+1]:
        r +=1
        any = q[i+1]
    else:
        if max(q[i+1:]) < any:
            any = q[i+1]
print(r+1)
