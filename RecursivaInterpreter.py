#--------------<Built-in Functions>--------------

add					= lambda x,y:x+y
subtract			= lambda x,y:x-y
multiply			= lambda x,y:x*y
divide				= lambda x,y:x/y
minusOne			= lambda x:x-1
square				= lambda x:x**2
rangeInclusive		= lambda x:[i for i in range(1,x+1)]
rangeExclusive		= lambda x:[i for i in range(1,x)]

dictionary={
	'¬':{'func':minusOne,'args':1},
	'+':{'func':add,'args':2},
	'-':{'func':subtract,'args':2},
	'*':{'func':multiply,'args':2},
	'/':{'func':divide,'args':2},
	'R':{'func':rangeInclusive,'args':1},
	'r':{'func':rangeExclusive,'args':1},
	'S':{'func':square,'args':1},
}

#--------------<Built-in Functions/>-------------

def atomicInterpret(atom,arguments):
	if len(arguments)==1:return dictionary[atom]['func'](arguments[0])
	if len(arguments)==2:return dictionary[atom]['func'](arguments[1],arguments[0])

def isIntLiteral(x):
	return x in[str(i) for i in range(10)]
 
def tokenizer(statement):
	tokens,i,j=[],0,0
	while i<len(statement):
		token=statement[i]
		if isIntLiteral(token):
			j=1
			while i+j<len(statement)and isIntLiteral(statement[i+j]):
				token+=statement[i+j];j+=1
			i+=j;tokens+=[int(token)]
		else:
			if token==' 'or token=='	':
				i+=1
			else:
				i+=1
				tokens+=[token]
	return tokens

def evaluate(statement):
	operatorStack=[]
	operandStack=[]
	for token in tokenizer(statement):
		if token in dictionary.keys():
			operatorStack.append(token)
		else:
			operandStack.append(token)
		if operatorStack and len(operandStack)>=dictionary[operatorStack[-1]]['args']:
			operands=[]
			argsLeft = dictionary[operatorStack[-1]]['args']
			while argsLeft:
				operands.append(operandStack.pop())
				argsLeft-=1
			operandStack.append(atomicInterpret(operatorStack.pop(),operands))
	while operatorStack:
		operator=operatorStack.pop()
		try:
			operand=operandStack.pop()
			operandStack.append(atomicInterpret(operator,operand))
		except:
			print("Too Few Operands")
			raise Exception
	result = operandStack.pop()
	if operandStack:
		print("Too many operands")
		raise Exception
	return result 
	
def interpret(statement):
	try:
		return str(evaluate(statement))
	except:
		raise Exception