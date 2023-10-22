from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("<h1><a href='9th'>9Th Grade</a></h1><h1><a href='9th-admin'>Admin</a></h1><h1><a "
                        "href='home'>Quizz</a>")
