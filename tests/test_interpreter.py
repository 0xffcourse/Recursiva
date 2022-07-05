from recursiva.interpreter import Interpreter

import unittest
from unittest.mock import patch
from io import StringIO


class OperatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.interpreter = Interpreter()

    def setUp(self):
        self.interpreter.resetMemory()

    def test_adder(self):
        self.assertEqual(self.interpreter.interpret("+ 8 9"), 17)

    def test_subtract(self):
        self.assertEqual(self.interpreter.interpret("- 9 5"), 4)

    def test_multiply(self):
        self.assertEqual(self.interpreter.interpret("*8 9"), 72)

    def test_divide(self):
        self.assertEqual(self.interpreter.interpret("/ 5 4"), 1.25)

    def test_character(self):
        self.assertEqual(self.interpreter.interpret("C 65"), "A")

    def test_stringer(self):
        self.assertEqual(self.interpreter.interpret("V 78"), "78")

    def test_getPiece(self):
        self.assertEqual(self.interpreter.interpret("Y [1,5,6,15,5] 3"), 15)
        self.assertEqual(self.interpreter.interpret("Y 'testing' 3"), 't')

    def test_listify(self):
        self.assertEqual(self.interpreter.interpret("A 45"), [45])

    def test_sliceFromLeft(self):
        self.assertEqual(self.interpreter.interpret("T [4,56,6]"), [56, 6])
        self.assertEqual(self.interpreter.interpret("T 'manna'"), 'anna')

    def test_integerer(self):
        self.assertEqual(self.interpreter.interpret("I 89.99"), 89)
        self.assertEqual(self.interpreter.interpret("I '89'"), 89)

    def test_floater(self):
        self.assertEqual(self.interpreter.interpret("F '89.90'"), 89.9)

    def test_minusOne(self):
        self.assertEqual(self.interpreter.interpret("~ 8"), 7)

    def test_plusOne(self):
        self.assertEqual(self.interpreter.interpret("; 45"), 46)

    def test_square(self):
        self.assertEqual(self.interpreter.interpret("S 19"), 361)

    def test_order(self):
        self.assertEqual(self.interpreter.interpret("O 'A'"), 65)

    def test_compare(self):
        self.assertEqual(self.interpreter.interpret("=9 9"), True)
        self.assertEqual(self.interpreter.interpret("=9 '9'"), False)

    def test_lesserThan(self):
        self.assertEqual(self.interpreter.interpret("<6 7"), True)

    def test_greaterThan(self):
        self.assertEqual(self.interpreter.interpret(">6 7"), False)

    def test_printer(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.interpreter.interpret("P 'Kana'")
            self.assertEqual(fakeOutput.getvalue(), 'Kana\n')

    def test_ander(self):
        self.assertEqual(self.interpreter.interpret("& 1 1"), True)

    def test_orer(self):
        self.assertEqual(self.interpreter.interpret("| 0 0"), False)

    def test_moder(self):
        self.assertEqual(self.interpreter.interpret("% 10 7"), 3)

    def test_doubler(self):
        self.assertEqual(self.interpreter.interpret("D 67"), 134)

    def test_halver(self):
        self.assertEqual(self.interpreter.interpret("H 78"), 39.0)

    def test_length(self):
        self.assertEqual(self.interpreter.interpret("L [6,7,8]"), 3)

    def test_slice(self):
        self.assertEqual(self.interpreter.interpret(
            "Z 4 'mandirabedi' 7"), "ira")
        self.assertEqual(self.interpreter.interpret(
            "Z4['m','an','dira',5,6,8,'bedi']7"), [6, 8, 'bedi'])

    def test_squareRoot(self):
        self.assertEqual(self.interpreter.interpret("R 9"), 3)

    def test_appendNewLine(self):
        self.assertEqual(self.interpreter.interpret("G \"old\""), "old/n")

    def test_joinWithNewLine(self):
        self.assertEqual(self.interpreter.interpret(
            "E ['the','blojj','spills']"), "the/nblojj/nspills")

    def test_joiner(self):
        self.assertEqual(self.interpreter.interpret(
            "J 'o' ['al','pal','ral']"), "alopaloral")

    def test_stringify(self):
        self.assertEqual(self.interpreter.interpret(
            "W [1,2,3,4]"), ["1", "2", "3", "4"])

    def test_ranger(self):
        self.assertEqual(self.interpreter.interpret("B4"), [1, 2, 3, 4])

    def test_splitter(self):
        self.assertEqual(self.interpreter.interpret(
            "Q 'alopaloral' 'o'"), ['al', 'pal', 'ral'])

    def test_exponent(self):
        self.assertEqual(self.interpreter.interpret("^ 2 6"), 64)

    def test_pythonEval(self):
        self.assertEqual(self.interpreter.interpret("U '7**2'"), 49)

    def test_pythonExec(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.interpreter.interpret("K 'print(45)'")
            self.assertEqual(fakeOutput.getvalue(), '45\n')

    def test_recursivaEval(self):
        self.assertEqual(self.interpreter.interpret("M '+*8 9 5'"), 77)

    def test_isIn(self):
        self.assertEqual(self.interpreter.interpret("N 'women' 'men'"), True)
        self.assertEqual(self.interpreter.interpret(
            "N ['wo','men'] 'men'"), True)

    def test_reverse(self):
        self.assertEqual(self.interpreter.interpret("_ 'murder'"), 'redrum')

    def test_stringReplace(self):
        self.assertEqual(self.interpreter.interpret(
            "r 'gentleman' 'magentleman' 'lady' "), "malady")

    def test_mapper(self):
        self.assertEqual(self.interpreter.interpret(
            "m [1,2,3,4]'Sa'"), [1, 4, 9, 16])
        # mapper string bug
        self.assertEqual(self.interpreter.interpret(
            "m ['maya','tyui']'La'"), [4, 4])

    def test_getValue(self):
        self.interpreter.setValue(45, "grand")
        self.assertEqual(self.interpreter.interpret("? 45"), "grand")

    def test_palindromizer(self):
        self.assertEqual(self.interpreter.interpret("p 'race'"), "racecar")

    def test_joinWithNothing(self):
        self.assertEqual(self.interpreter.interpret(
            "j ['s','p','e','l','l']"), 'spell')

    def test_summer(self):
        self.assertEqual(self.interpreter.interpret("s [1,2,3,4,5,6]"), 21)

    def test_fnder(self):
        self.assertEqual(self.interpreter.interpret("x 'i' 'find'"), 1)

    def test_sorter(self):
        self.assertEqual(self.interpreter.interpret(
            "k [1,2,3,4]'/ 1 a'"), [4, 3, 2, 1])

    def test_noOperation(self):
        self.assertEqual(self.interpreter.interpret(" 898"), 898)

    def test_assign(self):
        self.interpreter.interpret("` 4 [12,89]")
        self.assertEqual(self.interpreter.getValue(4), [12, 89])

    def test_upperAlphabet(self):
        self.assertEqual(self.interpreter.interpret(
            "("), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_lowerAlphabet(self):
        self.assertEqual(self.interpreter.interpret(")"),
                         "abcdefghijklmnopqrstuvwxyz")

    def test_forEach(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.interpreter.interpret("{B3 'P\"hegde\"'")
            self.assertEqual(fakeOutput.getvalue(), 'hegde\nhegde\nhegde\n')

    def test_whiler(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.interpreter.setValue(56, 3)
            self.interpreter.interpret("w'?56''&P15 `56~?56'")
            self.assertEqual(fakeOutput.getvalue(), '15\n15\n15\n')


class FeatureTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.interpreter = Interpreter()

    def setUp(self):
        self.interpreter.resetMemory()

    def test_conditional(self):
        self.assertEqual(self.interpreter.interpret("<4 5:1!100"), 1)
        self.assertEqual(self.interpreter.interpret("<5 5:1!100"), 100)
        # nested conditionals
        self.assertEqual(self.interpreter.interpret(
            ">a39:>a49:>a59:>a74:'dist'!'1st div'!'2nd div'!'3rd div'!'fail'@75"), 'dist')
        self.assertEqual(self.interpreter.interpret(
            ">a39:>a49:>a59:>a74:'dist'!'1st div'!'2nd div'!'3rd div'!'fail'@60"), '1st div')
        self.assertEqual(self.interpreter.interpret(
            ">a39:>a49:>a59:>a74:'dist'!'1st div'!'2nd div'!'3rd div'!'fail'@50"), '2nd div')
        self.assertEqual(self.interpreter.interpret(
            ">a39:>a49:>a59:>a74:'dist'!'1st div'!'2nd div'!'3rd div'!'fail'@40"), '3rd div')
        self.assertEqual(self.interpreter.interpret(
            ">a39:>a49:>a59:>a74:'dist'!'1st div'!'2nd div'!'3rd div'!'fail'@39"), 'fail')

    def test_function(self):
        self.assertEqual(self.interpreter.interpret("++^a2^b2D*ab@4 5"), 81)

    def test_recursive_function(self):
        self.assertEqual(self.interpreter.interpret("=a1:1!+~Da#~a$@4"), 16)
        # double params
        self.assertEqual(self.interpreter.interpret("<a3:1!+#~a$#~~a$@10"), 55)


class DocumentedTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.interpreter = Interpreter()

    def setUp(self):
        self.interpreter.resetMemory()

    def test_all_tests(self):
        self.assertEqual(self.interpreter.interpret("=a0:0!+a#~a$@100"), 5050)
        self.assertEqual(self.interpreter.interpret("Y_+B5A3IH1"), 3)
        self.assertEqual(self.interpreter.interpret(
            "Zba-Lac@[6,2,4,3,5,1,3] 5 0"), [1, 3])
        self.assertEqual(self.interpreter.interpret("*Ha+-Sa*3a4@40"), 29680.0)
