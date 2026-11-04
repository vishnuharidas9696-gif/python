n=int(input('enter a positive number:'))
e=int(input('enter the value exponent:'))
p=1
for i in range(1,e+1):
    p=p*n
print("The power of",n,"^",e,"is",p)