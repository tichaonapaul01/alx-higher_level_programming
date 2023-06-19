import unittest

def func1(a, b):
    return a + b

class TestBase(unittest.TestCase):
    def test1(self):
        result = func1(1, 2)
        self.assertEqual(result, 3)

    def test2(self):
        result = func1(4, 3)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
