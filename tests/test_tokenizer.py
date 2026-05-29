from recursiva.tokenizer import tokenize

import unittest


class TokenizerTest(unittest.TestCase):
    def test_simple_tokens(self):
        self.assertEqual(tokenize("+ 9 0"), [
            "+",
            "9",
            "0"
        ])

    def test_numeric_tokens(self):
        self.assertEqual(tokenize("-45"), [
            "-45"
        ])
        self.assertEqual(tokenize("- -45 4"), [
            "-",
            "-45",
            "4"
        ])
        self.assertEqual(tokenize("-+4.5 4 -1.365"), [
            "-",
            "+",
            "4.5",
            "4",
            "-1.365"
        ])

    def test_string_tokens(self):
        self.assertEqual(tokenize("+'man' 'tan'"), [
            '+',
            "'man'",
            "'tan'"
        ])
        self.assertEqual(tokenize("+'man' \"tan\""), [
            '+',
            "'man'",
            "\"tan\""
        ])

    def test_list_tokens(self):
        self.assertEqual(tokenize("+[9,0][8,9]"), [
            "+",
            "[9,0]",
            "[8,9]"
        ])
        self.assertEqual(tokenize("+[\"banana\",'alu'] ['bhalu'] \"malu\""), [
            "+",
            "[\"banana\",'alu']",
            "['bhalu']",
            "\"malu\""
        ])
