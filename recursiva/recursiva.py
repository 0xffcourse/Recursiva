from recursiva.interpreter import Interpreter

import sys


class Recursiva:

    def __init__(self):
        self._interpreter = Interpreter()

    # Behaves as an REPL
    def _repl(self):
        while 1:
            inString = input(">> ")
            if inString == "q":
                break
            try:
                outPut = self._interpreter.interpret(inString)
                if str(outPut) != 'None':
                    print('=> '+str(outPut).replace('/n', '\n'))
            except:
                print("=> Error!")
        exit()

    # Read code and inputs from file
    def _fire(self, code_file_path, input_file_path=None):
        try:
            code = inputted = ''
            with open(code_file_path) as code_file:
                for row in code_file:
                    code = row
            code_file.close()
            if input_file_path:
                with open(input_file_path) as input_file:
                    for row in input_file:
                        inputted = row
                input_file.close()
                if inputted:
                    code += '@'+inputted
            outPut = self._interpreter.interpret(code)
            if str(outPut) != 'None':
                print(str(outPut).replace('/n', '\n'))
        except:
            print("Error!")

    def run(self, argv):
        if len(argv) == 1:
            self._repl()
        else:
            if len(argv) == 2:
                self._fire(argv[1])
            else:
                self._fire(argv[1], argv[2])
