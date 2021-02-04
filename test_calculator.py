import unittest
import calculator

class TestCube(unittest.TestCase):
   def test1(self):
      self.assertEqual(calculator.addition(7, 5), 12)
      self.assertEqual(calculator.addition(10, 20), 30)
      self.assertEqual(calculator.addition(6, 9), 15)
      self.assertEqual(calculator.addition(-10, -5), -15)


   def test2(self):
      self.assertEqual(calculator.subtraction(7, 5), 2)
      self.assertEqual(calculator.subtraction(10, 20), -10)
      self.assertEqual(calculator.subtraction(6, 9), -3)
      self.assertEqual(calculator.subtraction(-10, -5), -5)

   def test3(self):
      self.assertEqual(calculator.multiplication(7, 5), 35)
      self.assertEqual(calculator.multiplication(10, 20), 200)
      self.assertEqual(calculator.multiplication(6, 9), 54)
      self.assertEqual(calculator.multiplication(-10, -5), 50)

   def test4(self):
      self.assertEqual(calculator.division(7, 5), 1.4)
      self.assertEqual(calculator.division(10, 20), 0.5)
      self.assertEqual(calculator.division(6, 9), 0.7)
      self.assertEqual(calculator.division(-10, -5), 2)
      self.assertRaises(ZeroDivisionError)


if __name__ == '__main__':
   unittest.main(verbosity = 2)
