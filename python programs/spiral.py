def spiralprint(m,n,a):
    k=0
    l=0
    while(k<m and l<n):
        for i in range(l,n):
            print(a[k][i])
        k+=1
        for i in range(k,m):
            print(a[i][n-1])
        n-=1
        if(k<m):
            for i in range(n-1,l-1,-1):
                print(a[m-1][i])
        m-=1
        if(l<n):
            for i in range(m-1,k-1,-1):
                print(a[i][l])
        l+=1
matrix=[]
R=int(input("Enter the no of rows: "))
c=int(input("Enter the no of columns: "))
print("Enter the values in to the matrix")
for i in range(R):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
spiralprint(R,c,matrix)
