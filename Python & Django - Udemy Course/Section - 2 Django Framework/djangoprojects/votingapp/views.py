from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    arr = ["Java", "Python", "CPlusPlus", "JavaScript", "PHP", "SQL"]
    mydictionary = {"arr": arr}
    return render(request, "index.html", context=mydictionary)


def getquery(request):
    q = request.GET[""]
    return HttpResponse(q)
