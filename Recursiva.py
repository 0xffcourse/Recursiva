import RecursivaInterpreter,os

os.system('cls')
os.system("color 1E")

running = True
while running:
 inString=input(">>")
 if inString=="q":running=False;continue;
 print('=>'+RecursivaInterpreter.interpret(inString))