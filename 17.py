p,q = input().split()
q= int(q)
fake = False
s = list(map(int,input().split()))
for i in range(len(s)):
    for j in range(len(s)):
        if s[i]+s[j] == q:
            fake = True
print("yes" if fake else "no") 
