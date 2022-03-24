import unittest

def checkDivisibleby7(x):
    if x % 7 == 0:
        return True
    else:
        return False

class Divsibleby7App(unittest.TestCase):

    def test_divby7_check(self):
        a = 14
        result = checkDivisibleby7(a)
        self.assertTrue(result)

    def test_divby7_check2(self):
        a = 9
        result = checkDivisibleby7(a)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

