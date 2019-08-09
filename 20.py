p,q=map(int,input().split())
r=list(map(int,input().split()))
r.sort()
r.reverse()
s=q
pin=0
for i in r:
    if(s>=i):
        any=int(s/i)
        pin=pin+any
        s=s-any*i
    if s==0:
        break
if(s==0):
   print(pin)
else:
   print("it's not posiible to select coins in such a way that they sum upto",king)
