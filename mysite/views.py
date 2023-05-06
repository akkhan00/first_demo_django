from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    params = {"name": "ahmad", "age": 14}
    return render(request, "index.html", params)

def removepunc(request)->HttpResponse:
    text = request.POST.get("textval", "default")
    return HttpResponse(text)

def analyze(request):
    text = request.POST.get("textval", "default")
    isremovePunc = request.POST.get("removepunc", "off")
    isuppercase = request.POST.get("touppercase", "off")
    isremovenewline = request.POST.get("removenewline", "off")
    isextraspaceremover = request.POST.get("extraspaceremove", "off")
    params = {"text":text, "purpose": "general"}
    if isremovePunc == "on":
        newText = ""
        punclist = "~`@#$%^&*()_-+={[\|';!:/?.><,\"]}"
        for char in text:
            if char not in punclist:
                newText += char
        text = newText
    if(isuppercase == "on"):
        text = text.upper()
    if(isremovenewline == "on"):
        newText = ""
        for ch in text:
            if(ch == "\n" or ch == "\r"):
                continue
            newText += ch
        text = newText
    if(isextraspaceremover== "on"):
        newText = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                newText += char
        text = newText
    params["text"] = text
    return render(request, "analyze.html", params)

def about(request)->HttpResponse:
    return HttpResponse(b"<h1>About</h1>")
