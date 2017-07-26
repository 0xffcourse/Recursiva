import RecursivaInterpreter,os

os.system('cls')
os.system("color 1E")

while 1:
	inString=input(">>")
	if inString=="q":break;
	try:print('=>'+str(RecursivaInterpreter.interpret(inString)))
	except:print("=>Parse Error")
	