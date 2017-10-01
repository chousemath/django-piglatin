from django.test import TestCase
from . import utility

class UtilityTestCase(TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_convert_to_piglatin(self):
    self.assertEqual(utility.convert_to_piglatin('fat'), 'atfay')

# @staticmethod
#     def map_over_string(original: str, func: Callable) -> str:
#         """Maps a function over a string"""
#         return ' '.join(list(map(func, original.split())))

#     @staticmethod
#     def convert_to_piglatin(original: str) -> str:
#         """Converts a word to its piglatin equivalent"""
#         first = original[0]
#         pig = ''
#         if first in VOWELS:
#             pig = original + 'way'
#         else:
#             pig = original[1:] + first + 'ay'
#         return pig

#     @staticmethod
#     def reverse_word(original: str) -> str:
#         """Reverses all the characters in the input word/phrase"""
#         reverse = ''
#         for character in original:
#             reverse = character + reverse
#         return reverse
