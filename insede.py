p,q=map(str,input().split())
w=0
if len(p)>len(q):
  p,q=q,s
i=0
while i<len(p):
  w+=(ord(q[i])-ord(p[i]))
  i+=1
for i in range(i,len(q)):
  w+=ord(q[i])-ord('a')+1
print(w)
