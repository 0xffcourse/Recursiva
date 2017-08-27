import sys

from repl import RCLI, rprint


sys.setrecursionlimit(1 << 30)

#--------------<Built-in Functions>--------------

adder			= lambda x,y:x+y
subtract		= lambda x,y:x-y
multiply		= lambda x,y:x*y
divide			= lambda x,y:x/y
character		= lambda x:chr(x)
stringer		= lambda x:type(x)==type('') and '"'+x+'"' or str(x)
piecefromlist	= lambda x,i:x[i]
listify			= lambda x:[x]
slicefromLeft	= lambda x:x[1:]
integerer		= lambda x:int(x)
floater			= lambda x:float(x)
minusOne		= lambda x:x-1
plusOne			= lambda x:x+1
square			= lambda x:x**2
order			= lambda x:ord(x)
compare			= lambda x,y:x==y
lesserThan		= lambda x,y:x<y
greaterThan		= lambda x,y:x>y
printer			= lambda x:rprint(str(x).replace('/n','\n'))
ander			= lambda x,y:x and y
orer			= lambda x,y:x or y
moder			= lambda x,y:x%y
doubler			= lambda x:2*x
halver			= lambda x:x/2
length			= lambda x:len(x)
slicestring		= lambda x,s,y:s[x:y]
squareroot		= lambda x:x**.5
appendnewline 	= lambda x:x+'/n'
joinwithnewline = lambda x:'/n'.join(map(str,x))
joiner			= lambda x,y:x.join(y)
stringify		= lambda x:[str(i) for i in x]
ranger			= lambda x:list(range(1,x+1))
splitter		= lambda x,a:x.split(a)
exponent		= lambda x,y:x**y
pythoneval		= lambda x:eval(x)
pythonexec		= lambda x:exec(x)
recursivaeval   = lambda x:interpret(x) 
stringin		= lambda x,y:y in x
reverse			= lambda x:x[::-1]

def foreach(x,y):
	for i in x:
		if type(x)==type('f'):interpret(y.replace('}','"'+str(i)+'"'))
		else:interpret(y.replace('}',' '+str(i)+' '))

dictionary={
	'{':{'func':foreach,'args':2},
	'_':{'func':reverse,'args':1},
	'A':{'func':listify,'args':1},
	'G':{'func':appendnewline,'args':1},
	'W':{'func':stringify,'args':1},
	'V':{'func':stringer,'args':1},
	'U':{'func':pythoneval,'args':1},
	'N':{'func':stringin,'args':2},
	'M':{'func':recursivaeval,'args':1},
	'K':{'func':pythonexec,'args':1},
	'J':{'func':joiner,'args':2},
	'~':{'func':minusOne,'args':1},
	';':{'func':plusOne,'args':1},
	'D':{'func':doubler,'args':1},
	'C':{'func':character,'args':1},
	'O':{'func':order,'args':1},
	'H':{'func':halver,'args':1},
	'+':{'func':adder,'args':2},
	'-':{'func':subtract,'args':2},
	'*':{'func':multiply,'args':2},
	'/':{'func':divide,'args':2},
	"I":{'func':integerer,'args':1},
	"F":{'func':floater,'args':1},
	"E":{'func':joinwithnewline,'args':1},
	"^":{'func':exponent,'args':2},
	'%':{'func':moder,'args':2},
	"R":{'func':squareroot,'args':1},
	'S':{'func':square,'args':1},
	'Z':{'func':slicestring,'args':3},
	'T':{'func':slicefromLeft,'args':1},
	'Y':{'func':piecefromlist,'args':2},
	'L':{'func':length,'args':1},
	'<':{'func':lesserThan,'args':2},
	'>':{'func':greaterThan,'args':2},
	'=':{'func':compare,'args':2},
	'&':{'func':ander,'args':2},
	'|':{'func':orer,'args':2},
	'P':{'func':printer,'args':1},
	'B':{'func':ranger,'args':1},
	'Q':{'func':splitter,'args':2}
}

#--------------<Built-in Functions/>-------------
 
def tokenizer(statement):
	tokens,i,j=[],0,0
	while i<len(statement):
		token=statement[i]
		if token in '0123456789.':
			j=1
			while i+j<len(statement)and statement[i+j]in '0123456789.':
				token+=statement[i+j];j+=1
			i+=j;tokens+=[token]
		elif token=='"':
			j=1
			token=''
			while i+j<len(statement)and statement[i+j]!='"':
				token+=statement[i+j];j+=1
			i+=j+1;tokens+=['"'+token+'"']
		elif token=="'":
			j=1
			token=''
			while i+j<len(statement)and statement[i+j]!="'":
				token+=statement[i+j];j+=1
			i+=j+1;tokens+=["'"+token+"'"]
		elif token=='[':
			j=1
			token=''
			while i+j<len(statement)and statement[i+j]!=']':
				token+=statement[i+j];j+=1
			i+=j+1;tokens+=['['+token+']']
		elif token==' 'or token=='	':
			i+=1
		elif token=='-':
			j=1
			while i+j<len(statement)and statement[i+j]in '0123456789.':
				token+=statement[i+j];j+=1
			i+=j
			tokens+=[token]
		else:
			i+=1
			tokens+=[token]
	return tokens

def evaluate(expression):
	operandStack=[]
	for token in tokenizer(expression)[::-1]:
		if token in dictionary.keys():
			if len(operandStack)<dictionary[token]['args']:raise Exception
			operands=[]
			argsLeft = dictionary[token]['args']
			while argsLeft:
				operands.append(eval(operandStack.pop()))
				argsLeft-=1
			calc=dictionary[token]['func'](*operands)
			if type(calc)==type(""):operandStack.append("'"+calc+"'") #place string under quotes
			else:operandStack.append(str(calc))
		else:
			operandStack.append(token)
	result = eval(operandStack.pop())
	if operandStack:
		raise Exception
	return result

def function_interpret(function_statement):
	function_statement=function_statement[::-1]
	arguments_string = function_statement[:function_statement.find('@')][::-1]
	function_string = function_statement[function_statement.find('@')+1:][::-1]
	arguments = arguments_string.split()
	compiled = tokenizer(function_string)
	alphas=[i for i in compiled if len(i)==1 and 'a'<=i<='f']
	if alphas:
		start_alpha=min(alphas)
		for i,x in enumerate(compiled):
			if len(x)==1 and 'a'<=x<='f':compiled[i]=' '+arguments[ord(x)-ord(start_alpha)]+' '
	compiled=''.join(compiled)
	try:
		return interpret(compiled)
	except:
		#probably is recursive, lets reduce it
		recursive=compiled.count('$')*['']
		compiled_inverted= compiled[::-1]
		i=0
		for n,x in enumerate(recursive):
			while compiled_inverted[i]!='$':i+=1 
			recursive[n]='$';i+=1
			while compiled_inverted[i]!='#':recursive[n]=compiled_inverted[i]+recursive[n];i+=1
			recursived=interpret(recursive[n][:-1])
			if type(recursived)==type(""):recursived=("'"+recursived+"'") #place string under quotes
			if type(recursived)==type([]):recursived="["+','.join(str(i)for i in recursived)+"]"
			else:recursived=str(recursived)
			compiled = compiled.replace('#'+recursive[n], ' '+str(interpret(function_string+'@'+recursived))+' ')
		return interpret(compiled) 

def interpret(statement):
	try:
		if '@' in tokenizer(statement):
			return function_interpret(statement)
		if ':' in tokenizer(statement):
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

#Behaves as an REPL
if len(sys.argv)==1:
	with RCLI() as cli:
		#initialize rprint by enclosing current_buffer
		rprint = rprint(cli.current_buffer)

		while 1:

			doc = cli.run()
			if doc.text=="q":break;
			try:
				outPut=interpret(doc.text.rstrip(';;'))
				if str(outPut)!='None':rprint('=> '+str(outPut).replace('/n','\n'))
			except:rprint("=> Error!")
			finally:
				cli.current_buffer.inc()
		exit()

#Read code and inputs from file
try:
	code=inputted=''
	code_file_path = sys.argv[1]
	with open(code_file_path) as code_file:
		for row in code_file:
			code=row
	code_file.close()
	if len(sys.argv)==3:
		input_file_path = sys.argv[2]
		with open(input_file_path) as input_file:
			for row in input_file:
				inputted=row
		input_file.close()
		if inputted:code+='@'+inputted
	outPut=interpret(code)
	if str(outPut)!='None':rprint(str(outPut).replace('/n','\n'))
except:rprint("Error!")