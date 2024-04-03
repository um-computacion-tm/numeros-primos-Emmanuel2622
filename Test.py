from Primo import is_primo
import unittest

class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, True)

    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)
    
    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, True)

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, True)

    def test_7(self):
        result = is_primo(7)
        self.assertEqual(result, True)

    def test_8(self):
        result = is_primo(8)
        self.assertEqual(result, True)

    def test_9(self):
        result = is_primo(9)
        self.assertEqual(result, True)
    
    def test_10(self):
        result = is_primo(10)
        self.assertEqual(result, True)

    def test_11(self):
        result = is_primo(11)
        self.assertEqual(result, True)

unittest.main()