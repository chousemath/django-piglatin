from typing import Callable

VOWELS = ['a', 'e', 'i', 'o', 'u']

def map_over_string(original: str, func: Callable) -> str:
    """Maps a function over a string"""
    return ' '.join(list(map(func, original.split())))

def convert_to_piglatin(original: str) -> str:
    """Converts a word to its piglatin equivalent"""
    first = original[0]
    pig = ''
    if first in VOWELS:
        pig = original + 'way'
    else:
        pig = original[1:] + first + 'ay'
    return pig

def reverse_word(original: str) -> str:
    """Reverses all the characters in the input word/phrase"""
    reverse = ''
    for character in original:
        reverse = character + reverse
    return reverse
