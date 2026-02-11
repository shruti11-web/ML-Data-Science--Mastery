'''Type Casting in Python
   * Implicit Typecasting (convert automatically)
   * Explicit Typecasting(changes manually by programmer)
'''
a=7
print(type(a))
b=3.0
print(type(b))
c=a+b
print(c)
print(type(c))
d=a*b
print(d)
print(type(d))


#Eplicit Typecasting

a=5
n=float(a)
print(n)
print(type(n))
p=str(n)
print(p)
print(type(p))
q=float(p)
print(q)
print(type(q))

a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=a*b
print(c)
n=float(c)
print(n)
print(type(n))