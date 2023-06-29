from random import*
d=sample(range(10), 4)
s=(input("Enter the number:"))
l=[]
b=""
for i in range(4):
    a=int(s[i])
    l.append(a)
for i in range(4):
    if(l[i] in d):
        if(l[i]==d[i]):
            b=b+"+"
        else:
            b=b+"-"
    else:
        b=b+"*"
n=""
for i in d:
    i=str(i)
    n=n+i
n=int(n)
print("The computer generated number is:",n)
print(b)
    
