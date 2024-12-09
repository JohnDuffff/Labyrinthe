import unittest

def Multiplication(a, b):
    return a*b

class TestMultiplication(unittest.TestCase):
    def test_multiplication_positives(self):
        self.assertEqual(Multiplication(2, 3), 6)  #Test 2 positifs

    def test_multiplication_negatives(self):
        self.assertEqual(Multiplication(-2, -3), 6)  #Test 2 négatifs

    def test_multiplication_mix(self):
        self.assertEqual(Multiplication(2, -3), -6)  #Test positif + négatif

    def test_multiplication_virgules(self):
        self.assertEqual(Multiplication(2.5, 3.1), 7.75)  #Test nombres à virgule


if __name__ == "__main__":
    unittest.main()