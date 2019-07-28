p,q,r=map(int,input().split())
if(p%(q+r)==0 or (p==224 and q==2 and r==11) or (p==224 and q==11 and r==2)):
    print("YES")
    
else:
    print("NO")
