a=int(input())
p=1
while(p<=a and p*2<=a):
    p=p*2
if(p==a):
    print("0")
else:    
    print(a-p)
