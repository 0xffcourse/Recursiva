#--------------<Built-in Functions>--------------

minusOne       = lambda x:x-1
add            = lambda x,y:x+y
square         = lambda x:x**2
rangeInclusive = lambda x:rangeExclusive(x)+[x]
rangeExclusive = lambda x:[i for i in range(1,x)]
printer        = lambda x:print(x) 

dictionary={
	'¬':{'func':minusOne,'args':1},
	'+':{'func':add,'args':2},
	'R':{'func':rangeInclusive,'args':1},
	'r':{'func':rangeExclusive,'args':1},
	'S':{'func':square,'args':1},
	'P':{'func':printer,'args':1}
}

#--------------<Built-in Functions/>-------------

def atomicInterpret(atom,arguments):
	if len(arguments)==1:return dictionary[atom]['func'](arguments[0])
	if len(arguments)==2:return dictionary[atom]['func'](arguments[0],arguments[1])
	if len(arguments)==3:return dictionary[atom]['func'](arguments[0],arguments[1],arguments[2])

def isIntLiteral(x):
	return x in[str(i) for i in range(10)]
 
def tokenizer(statement):
	tokens,i,j=[],0,0
	while i<len(statement):
		token=statement[i]
		if isIntLiteral(token):
			j=1
			while i+j<len(statement)and isIntLiteral(statement[i+j]):
				m=int(statement[i+j])
				token+=statement[i+j];j+=1
			i+=j;tokens+=[int(token)]
		else:
			if token==' 'or token=='	':i+=1
			else:i+=1;tokens+=[token]
	return tokens

def evaluate(statement):
	operatorStack=[]
	operandStack=[]
	for token in tokenizer(statement):
		if token in dictionary.keys():operatorStack.append(token)
		else:operandStack.append(token)
	while operatorStack:
		operator=operatorStack.pop()
		try:
			operands=[]
			argsLeft = dictionary[operator]['args']
			while argsLeft:
				operands.append(operandStack.pop())
				argsLeft-=1
			operandStack.append(atomicInterpret(operator,operands))
		except:
			raise Exception("Too few operands")
	result = operandStack.pop()
	if operandStack:raise Exception("Too many operands")
	return result 

def interpret(statement):
	try:return str(evaluate(statement))
	except:raise Exception("Parse error")