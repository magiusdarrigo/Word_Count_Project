from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordDictionary = {}


    for word in wordlist:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'dict': sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)})

def about(request):
    return render(request, 'about.html')