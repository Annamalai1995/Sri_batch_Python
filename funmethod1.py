#All
a=[0,1,2,3]
b=all(a)
print(b)
#any
a=(1,1,False)
b=any(a)
print(b)
#bin
a=bin(10)
print(a)
#boolean
a=bool(0)
print(a)
#bytearray
a=bytearray(5)
print(a)
#bytes
a=bytes(5)
print(a)
#callable
def a():
    b=15
print(callable(b))
print(callable(a))
#char
a=chr(6)
print(a)
#sum
a=sum([2,4,5])
print(a)