#--------------<Built-in Functions>--------------

minusOne       = lambda x:x-1
add            = lambda x,y:x+y
square         = lambda x:x**2
rangeInclusive = lambda x:rangeExclusive(x)+[x]
rangeExclusive = lambda x:[i for i in range(1,x)]
printer        = lambda x:print(x) 

dictionary={
	'¬':{'func':minusOne,'arg':1},
	'+':{'func':add,'arg':2},
	'R':{'func':rangeInclusive,'arg':1},
	'r':{'func':rangeExclusive,'arg':1},
	'S':{'func':square,'arg':1},
	'P':{'func':printer,'arg':1}
}

#--------------<Built-in Functions/>-------------

def atomicInterpret(atom,arguments):
	return dictionary[atom]['func'](arguments)

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
		operandStack+=[atomicInterpret(operatorStack.pop(),operandStack.pop())]
	return operandStack.pop()

def interpret(statement):
	return str(evaluate(statement))