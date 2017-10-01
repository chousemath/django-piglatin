"""Contains all view logic"""

from typing import Callable
from django.http import HttpResponse
from django.shortcuts import render

VOWELS = ['a', 'e', 'i', 'o', 'u']

def about(request):
    """Renders the about page"""
    return render(request, 'about.html')

def home(request):
    """Renders the home page with all text transform options"""
    return render(request, 'home.html')

def piglatin(request):
    """Page containing results of pig latin translation"""
    original = request.GET['phrase-piglatin']
    pigphrase = map_over_string(original, convert_to_piglatin)
    print(pigphrase)
    return render(request, 'piglatin.html', {
      'original': original,
      'transformed': pigphrase
    })

def reverse(request):
    """Page containing results of text reversal"""
    original_text = request.GET['phrase-reverse']
    print(original_text)
    return render(request, 'reverse.html')

def novowels(request):
    """Page containing results of vowel removal"""
    original_text = request.GET['phrase-no-vowels']
    print(original_text)
    return render(request, 'novowels.html')

def not_found(request):
    """Default page for unresolved routing"""
    return render(request, 'not_found.html')

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
