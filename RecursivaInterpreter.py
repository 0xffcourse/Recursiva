#--------------<Built-in Functions>--------------

minusOne = lambda x:x-1
add      = lambda x:sum(int(i) for i in x)
square   = lambda x:x**2

#--------------<Built-in Functions/>-------------

def atomicInterpret(atom,arguments):
 dictionary={
	'¬':minusOne,
	'+':add,
	'S':square
 }
 return dictionary[atom](arguments)

print(atomicInterpret('S',9))