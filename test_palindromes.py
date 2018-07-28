import unittest 
from palindromes import *

class TestPalindromes(unittest.TestCase):
	def test_output(self):
		self.assertEqual(palindrome('Kengo'), 'False, isn\'t palindrome.')
		self.assertEqual(palindrome('nurses run'), 'True, is palindrome.')
		self.assertEqual(palindrome('maddam'), 'True, is palindrome.')
		self.assertEqual(palindrome('22ksj!dn'), 'False, isn\'t palindrome.')