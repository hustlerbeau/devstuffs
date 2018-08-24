from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext= request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()

    wordcountdictionary = {}

    for word in wordlist:
        if word in wordcountdictionary:
            #Increase
            wordcountdictionary[word] += 1
        else:
            #add word to the dictionary
            wordcountdictionary[word] = 1

    sortedwords = sorted(wordcountdictionary.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})
