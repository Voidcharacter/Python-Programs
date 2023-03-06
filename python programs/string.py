s=str(input("Enter the string: "));
l=len(s)
s1=''
s2=''
r=''
if(l%2==0):
    for i in range(0,l//2):
        s1+=s[i]
    for j in range(l//2,l):
        s2+=s[j]
    for k in range(len(s1)-1,-1,-1):
        r+=s1[k]
        r+=s2[k]
print("Resultant string: ",r)
    
    
