b=str(input("Enter the no: "))
l=len(b)
n=int(b)
a=[]
outarr=[]
s=0
while(n>0):
    d=n%10
    s=s*10+d
    if(d%2!=0):
        outarr.append(d)
    a.append(d)
    n=n//10
outarr.append(s)
for i in range(0,l):
    s1=0
    s1=s1+a[i]
    for j in range(l-1,-1,-1):
        if(a[i]!=a[j]):
            s1=s1*10+a[j]
    if(s1%2!=0):
        outarr.append(s1)
print(outarr)
for i in range(0,len(outarr)):
    for j in range(i,len(outarr)):
        if(outarr[i]>outarr[j]):
            outarr[i]=outarr[i]+outarr[j]
            outarr[j]=outarr[i]-outarr[j]
            outarr[i]=outarr[i]-outarr[j]
print(outarr)
    
    
    
