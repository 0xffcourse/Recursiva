#--------------<Built-in Functions>--------------

add					= lambda x,y:x+y
subtract			= lambda x,y:x-y
multiply			= lambda x,y:x*y
divide				= lambda x,y:x/y
minusOne			= lambda x:x-1
square				= lambda x:x**2
compare				= lambda x,y:x==y
lesserThan			= lambda x,y:x<y
greaterThan			= lambda x,y:x>y
printer				= lambda x:print(x)

dictionary={
	'¬':{'func':minusOne,'args':1},
	'+':{'func':add,'args':2},
	'-':{'func':subtract,'args':2},
	'*':{'func':multiply,'args':2},
	'/':{'func':divide,'args':2},
	'S':{'func':square,'args':1},
	'<':{'func':lesserThan,'args':2},
	'>':{'func':greaterThan,'args':2},
	'=':{'func':compare,'args':2},
	'P':{'func':printer,'args':1}
}

#--------------<Built-in Functions/>-------------

def atomicInterpret(func,arguments):
	if len(arguments)==1:return dictionary[func]['func'](arguments[0])
	if len(arguments)==2:return dictionary[func]['func'](arguments[1],arguments[0])
 
def tokenizer(statement):
	tokens,i,j=[],0,0
	while i<len(statement):
		token=statement[i]
		if token in '0123456789':
			j=1
			while i+j<len(statement)and statement[i+j]in '0123456789':
				token+=statement[i+j];j+=1
			i+=j;tokens+=[int(token)]
		elif token==' 'or token=='	':
			i+=1
		elif token=='-':
			j=1
			while i+j<len(statement)and statement[i+j]in '0123456789':
				token+=statement[i+j];j+=1
			i+=j
			if j>1:tokens+=[int(token)] #- follwed by integer
			else:tokens+=[token]
		else:
			i+=1
			tokens+=[token]
	return tokens

def evaluate(expression):
	operatorStack=[]
	operandStack=[]
	for token in tokenizer(expression):
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
			raise Exception
	result = operandStack.pop()
	if operandStack:
		raise Exception
	return result

def function_interpret(function_statement):
	function_string = function_statement.split('@')[0]
	arguments_string = function_statement.split('@')[1]
	arguments = arguments_string.split()
	alphas=[i for i in function_string if 'a'<=i<='z']
	start_alpha=min(alphas)
	compiled = function_string
	for i,x in enumerate(arguments):
		compiled = compiled.replace(chr(ord(start_alpha)+i),str(interpret(x)))
	try:
		return str(interpret(compiled))
	except:
		#probably is recursive, lets reduce it
		recursive=compiled.count('$')*['']
		compiled_inverted= compiled[::-1]
		i=0
		for n,x in enumerate(recursive):
			while compiled_inverted[i]!='$':i+=1 
			recursive[n]='$';i+=1
			while compiled_inverted[i]not in ':!$+ ':recursive[n]=compiled_inverted[i]+recursive[n];i+=1
			recursived=str(interpret(recursive[n][:-1]))
			compiled = compiled.replace(recursive[n], ' '+str(interpret(function_string+'@'+recursived))+' ')
		return str(interpret(compiled)) 

def interpret(statement):
	try:
		if '@' in statement:
			return function_interpret(statement)
		if ':' in statement:
			condition=statement[:statement.find(':')]
			statements=statement[statement.find(':')+1:]
			statements_inverted=statements[::-1]
			if_statement=statements_inverted[statements_inverted.find('!')+1:][::-1]
			else_statement=statements_inverted[:statements_inverted.find('!')][::-1]
			if interpret(condition):return interpret(if_statement)
			if (else_statement):return interpret(else_statement)
			else:return None
		else:
			return evaluate(statement)
	except:
		raise Exception

while 1:
	inString=input(">>")
	if inString=="q":break;
	try:print('=>'+str(interpret(inString)))
	except:print("=>Parse-Error or Math-Error!")