from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request, 'home.html')

def count(request):
    data= request.GET['textvalue']
    word_list= data.split()
    length = len(word_list)

    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1


    return render(request, 'count.html', {'textvalue':data,'countword':length, 'worddic':word_dictionary.items()})
