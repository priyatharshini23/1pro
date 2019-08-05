p,q=map(int,input().split())
last=list(map(int,input().split()))
lin=[]
for i in range(0,q):
     a,b=map(int,input().split())
     lin.append([a,b])
for i in range(q):
     lower=lin[i][0]
     upper=lin[i][1]
     s=sum(last[lower-1:upper])
     print(s)
