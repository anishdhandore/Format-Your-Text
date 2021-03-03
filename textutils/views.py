from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")

def analyze(request):
    djtext = request.POST.get('text')
    punc = request.POST.get('punc')
    caps = request.POST.get('caps')
    space = request.POST.get('space')


    if punc == "on":
        punctuations = '''!()-[]{}|;:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char in punctuations:
                a = djtext.replace(char, ' ')
                djtext = a
        messages.success(request, 'Your text was analyzed!')
        params = {'purpose': 'Removed punctuations', 'analyzed_text': djtext}
        return render(request, 'analyze.html', context= params)
     
    if caps=="on":
        analyzed = djtext.upper()
        params = {'purpose': 'Capitalized text', 'analyzed_text': analyzed} 
        return render(request, 'analyze.html', context= params)
    
    if space=="on":
        for char in djtext:
            if char == ' ':
                a = djtext.replace(char, '')
                djtext = a
        params = {'purpose': 'Removing spaces', 'analyzed_text': djtext}
        return render(request, 'analyze.html', context= params)

    else:
        return redirect('/')
    
    
    



