"""Contains all view logic"""

from django.http import HttpResponse
from django.shortcuts import render
from . import utility

def about(request):
    """Renders the about page"""
    return render(request, 'about.html')

def home(request):
    """Renders the home page with all text transform options"""
    return render(request, 'home.html')

def piglatin(request):
    """Page containing results of pig latin translation"""
    original = request.GET['phrase-piglatin']
    pigphrase = utility.map_over_string(original, utility.convert_to_piglatin)
    print(pigphrase)
    return render(request, 'piglatin.html', {
        'original': original,
        'transformed': pigphrase
    })

def reverse_phrase(request):
    """Page containing results of text reversal"""
    original = request.GET['phrase-reverse']
    reverse_string = utility.map_over_string(original, utility.reverse_word)
    print(reverse_string)
    return render(request, 'reverse.html', {
        'original': original,
        'transformed': reverse_string
    })

def novowels(request):
    """Page containing results of vowel removal"""
    original_text = request.GET['phrase-no-vowels']
    print(original_text)
    return render(request, 'novowels.html')

def not_found(request):
    """Default page for unresolved routing"""
    return render(request, 'not_found.html')
