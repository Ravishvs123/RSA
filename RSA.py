import math
p=5
q=7
n=p*q
print("n=",n)
e=2
phi=(p-1)*(q-1)
while (e<phi):
    if (math.gcd (e,phi==1)):
        break
    else:
        e=e+1
        print("e=",e)
k=2
d=((k*phi)+1)/2
print("d=",d)
print(f'public ke={e,n}')
print(f'pravet ke={d,n}')
msg=11
print(f'message is={msg}')
print("message data is=",msg)
c=pow(msg,e)
c=math.fmod(c,n)
print("encrypt data",c)
m=pow(e,d)
m=math.fmod(m,n)
print("decrypt data",m)
        
        
