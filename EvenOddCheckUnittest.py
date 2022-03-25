import unittest

def check(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

class EvenOrAddApp(unittest.TestCase):

    def test_case_even_check(self):
        a = 10
        result = check(a)
        self.assertEqual("even", result)

    def test_case_odd_check(self):
        a = 7
        result = check(a)
        self.assertEqual("odd", result)

if __name__ == "__main__":
    unittest.main()

