from django.shortcuts import render


# Create your views here.
def index(request):
    arr = ["Java", "Python", "CPlusPlus", "JavaScript", "PHP", "SQL"]
    mydictionary = {"arr": arr}
    return render(request, "index.html", context=mydictionary)
