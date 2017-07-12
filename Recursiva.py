import RecursivaInterpreter,os

os.system('cls')
os.system("color 1E")

running = True
while running:
 print('=>'+RecursivaInterpreter.interpret(input(">>")))