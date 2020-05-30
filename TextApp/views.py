from django.shortcuts import render
from django.http import HttpResponse
def Home(request):
    return render(request,'Home.html')

def String(request):
    return render(request,'string.html')

def Remove(request):
    originalText=request.GET.get('text','default')
    remove=request.GET.get('removepunc','off')
    upperB=request.GET.get('upper','off')
    lowerB=request.GET.get('lower','off')
    titleB=request.GET.get('title','off')
    resultText=originalText
    if remove=="on":
        tempText = ""
        list='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in   originalText:
            if char not in list:
                tempText=tempText+char
        resultText=tempText
    if upperB=="on":
        resultText=  resultText.upper()
    if lowerB=="on":
        resultText=  resultText.lower()
    if titleB=="on":
        resultText=  resultText.title()

    param= {'purpose':'Remove punctuation', 'resultText':resultText}
    return render(request,'result.html',param)
