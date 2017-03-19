import unittest
import rpn
class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('2 3 ^')
		self.assertEqual(8, result)
	def test_subtract(self):
		result = rpn.calculate('3 3 ^')
		self.assertEqual(27, result)