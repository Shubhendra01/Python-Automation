import unittest

def volumeofcube(x):
    return (x*x*x)

class Cube_volumeApp(unittest.TestCase):

    def test_case_cubevolume(self):
        a = 5.555
        result = volumeofcube(a)
        self.assertAlmostEqual(result, a*a*a)

if __name__ == "__main__":
    unittest.main()
