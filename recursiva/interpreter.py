from recursiva.tokenizer import tokenize
from recursiva.operators import dictionary

import sys


class Interpreter:

    def __init__(self):
        # set high recursion limit
        sys.setrecursionlimit(1 << 30)
        # initiate memory
        self._values = {}
        self.resetMemory()

    def _evaluate(self, expression):
        operandStack = []
        for token in tokenize(expression)[::-1]:
            if token in dictionary.keys():
                if len(operandStack) < dictionary[token]['args']:
                    raise Exception
                operands = []
                argsLeft = dictionary[token]['args']
                while argsLeft:
                    operands.append(eval(operandStack.pop()))
                    argsLeft -= 1
                # pass self reference to builtins (if needed)
                if 'useInterpreterRef' in dictionary[token]:
                    operands.append(self)
                calc = dictionary[token]['func'](*operands)
                if type(calc) == type(""):
                    # place string under quotes
                    operandStack.append("'"+calc+"'")
                else:
                    operandStack.append(str(calc))
            else:
                operandStack.append(token)
        result = eval(operandStack.pop())
        if operandStack:
            raise Exception
        return result

    def _function_interpret(self, function_statement):
        function_statement = function_statement[::-1]
        arguments_string = function_statement[:function_statement.find(
            '@')][::-1]
        function_string = function_statement[function_statement.find(
            '@')+1:][::-1]
        arguments = tokenize(arguments_string)
        compiled = tokenize(function_string)
        alphas = [i for i in compiled if len(i) == 1 and 'a' <= i <= 'f']
        if alphas:
            start_alpha = min(alphas)
            for i, x in enumerate(compiled):
                if len(x) == 1 and 'a' <= x <= 'f':
                    compiled[i] = ' '+arguments[ord(x)-ord(start_alpha)]+' '
        compiled = ''.join(compiled)
        try:
            return self.interpret(compiled)
        except:
            # probably is recursive, lets reduce it
            recursive = compiled.count('$')*['']
            compiled_inverted = compiled[::-1]
            i = 0
            for n, x in enumerate(recursive):
                while compiled_inverted[i] != '$':
                    i += 1
                recursive[n] = '$'
                i += 1
                while compiled_inverted[i] != '#':
                    recursive[n] = compiled_inverted[i]+recursive[n]
                    i += 1
                recursived = self.interpret(recursive[n][:-1])
                if type(recursived) == type(""):
                    # place string under quotes
                    recursived = ("'"+recursived+"'")
                if type(recursived) == type([]):
                    recursived = "["+','.join(str(i)for i in recursived)+"]"
                else:
                    recursived = str(recursived)
                compiled = compiled.replace(
                    '#'+recursive[n], ' '+str(self.interpret(function_string+'@'+recursived))+' ')
            return self.interpret(compiled)

    def setValue(self, index, value):
        self._values[index] = value

    def getValue(self, index):
        return self._values[index]

    def resetMemory(self):
        for i in range(100):
            if i % 2 == 0:
                self._values[i] = 0
            else:
                self._values[i] = 1

    def interpret(self, statement):
        try:
            if '@' in tokenize(statement):
                return self._function_interpret(statement)
            if ':' in tokenize(statement):
                condition = statement[:statement.find(':')]
                statements = statement[statement.find(':')+1:]
                statements_inverted = statements[::-1]
                if_statement = statements_inverted[statements_inverted.find(
                    '!')+1:][::-1]
                else_statement = statements_inverted[:statements_inverted.find(
                    '!')][::-1]
                if self.interpret(condition):
                    return self.interpret(if_statement)
                if (else_statement):
                    return self.interpret(else_statement)
                else:
                    return None
            else:
                return self._evaluate(statement)
        except:
            raise Exception
