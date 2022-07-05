def adder(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


def character(x):
    return chr(x)


def stringer(x):
    return type(x) == type('') and '"'+x+'"' or str(x)


def getPiece(x, i):
    return x[i]


def listify(x):
    return [x]


def sliceFromLeft(x):
    return x[1:]


def integerer(x):
    return int(x)


def floater(x):
    return float(x)


def minusOne(x):
    return x-1


def plusOne(x):
    return x+1


def square(x):
    return x**2


def order(x):
    return ord(x)


def compare(x, y):
    return x == y


def lesserThan(x, y):
    return x < y


def greaterThan(x, y):
    return x > y


def printer(x):
    return print(str(x).replace('/n', '\n'))


def ander(x, y):
    return x and y


def orer(x, y):
    return x or y


def moder(x, y):
    return x % y


def doubler(x):
    return 2*x


def halver(x):
    return x/2


def length(x):
    return len(x)


def slice(x, s, y):
    return s[x:y]


def squareRoot(x):
    return x**.5


def appendNewLine(x):
    return x+'/n'


def joinWithNewLine(x):
    return '/n'.join(map(str, x))


def joiner(x, y):
    return x.join(y)


def stringify(x):
    return [str(i) for i in x]


def ranger(x):
    return list(range(1, x+1))


def splitter(x, a):
    return x.split(a)


def exponent(x, y):
    return x**y


def pythonEval(x):
    return eval(x)


def pythonExec(x):
    return exec(x)


def recursivaEval(x, interpreter):
    return interpreter.interpret(x)


def isIn(x, y):
    return y in x


def reverse(x):
    return x[::-1]


def stringReplace(a, x, b):
    return x.replace(str(a), str(b))


def mapper(a, b, interpreter):
    return [type(i) == type('x') and interpreter.interpret(
        b+'@\''+str(i)+'\'') or interpreter.interpret(b+'@'+str(i)) for i in a]


def getValue(a, interpreter):
    return interpreter.getValue(a)


def palindromizer(x):
    return x[:-1]+x[::-1]


def joinWithNothing(x):
    return ''.join(x)


def summer(x):
    return sum(x)


def finder(x, y):
    return y.index(x)


def sorter(x, y, interpreter):
    return sorted(x, key=lambda z: interpreter.interpret(y+"@"+str(z)))


def noOperation(x):
    return x


def assign(a, b, interpreter):
    interpreter.setValue(a, b)


def upperAlphabet():
    return'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def lowerAlphabet():
    return'abcdefghijklmnopqrstuvwxyz'


def forEach(x, y, interpreter):
    for i in x:
        if type(x) == type('f'):
            interpreter.interpret(y.replace('}', '"'+str(i)+'"'))
        else:
            interpreter.interpret(y.replace('}', ' '+str(i)+' '))


def whiler(x, y, interpreter):
    while(interpreter.interpret(x)):
        interpreter.interpret(y)
