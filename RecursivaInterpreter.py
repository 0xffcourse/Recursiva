#--------------<Built-in Functions>--------------

minusOne       = lambda x:x-1
add            = lambda x,y:x+y
square         = lambda x:x**2
rangeInclusive = lambda x:rangeExclusive(x)+[x]
rangeExclusive = lambda x:[i for i in range(1,x)]
printer        = lambda x:print(x) 

#--------------<Built-in Functions/>-------------

def atomicInterpret(atom,arguments):
	dictionary={
	'¬':minusOne,
	'+':add,
	'R':rangeInclusive,
	'r':rangeExclusive,
	'S':square,
	'P':printer
	}
	return dictionary[atom](arguments)

def isIntLiteral(x):
	return x in[str(i) for i in range(10)]
 
def tokenizer(statement):
	statement=''.join(statement.split())
	tokens,i,j=[],0,0
	while i<len(statement):
		token=statement[i]
		if isIntLiteral(token):
			j=1
			while i+j<len(statement)and isIntLiteral(statement[i+j]):
				m=int(statement[i+j])
				token+=statement[i+j];j+=1
			i+=j;tokens+=[int(token)]
		else:i+=1;tokens+=[token]
	return tokens

def evaluate(statement):
	stack=tokenizer(statement)
	while len(stack)>1:
		literal=stack.pop()
		function=stack.pop()
		stack+=[atomicInterpret(function,literal)]
	return stack.pop()

def interpret(statement):
	return str(evaluate(statement))