import unittest

def add(x, y):
    return x+y

class MyApp2(unittest.TestCase):

    def test_case3(self):
        a = 10
        b = 22
        result = add(a,b)
        self.assertEqual(a+b, result)

    def test_case4(self):
        a = 12.5
        b = 12.9
        result = add(a, b)
        self.assertEqual(a+b, result)

if __name__ == "__main__":
    unittest.main()
