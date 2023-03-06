import math
r=int(input("Enter the length of rows: "))
c=int(input("Enter the length of columns: "))
m=[]
d=[]

for i in range(0,r):
    a=[]
    for  j in range(0,c):
        a.append(int(input()))
    m.append(a)
outarr=[]
for l in range(0,4):
    product=1
    if(r==c):
        if(l==0):
            for i in range(0,r-1):
                for j in range(0,c-1):
                    d.append(m[i][j])
                    product*=m[i][j]
        elif(l==1):
            for i in range(0,r-1):
                for j in range(l,c-1+l):
                    d.append(m[i][j])
                    product*=m[i][j]
        elif(l==2):
            for i in range(1,r):
                for j in range(0,c-1):
                    d.append(m[i][j])
                    product*=m[i][j]
        elif(l==3):
            for i in range(1,r):
                for j in range(1,c):
                    d.append(m[i][j])
                    product*=m[i][j]
    print(product)
    s=int(math.sqrt(product))
    if((s*s)==product):
        outarr.append(product)
d=len(outarr)
for i in range(0,d-1):
    if(outarr[i]>outarr[i+1]):
        outarr[i]=outarr[i]+outarr[i+1]
        outarr[i+1]=outarr[i]-outarr[i+1]
        outarr[i]=outarr[i]-outarr[i+1]
print(outarr)

        



    
