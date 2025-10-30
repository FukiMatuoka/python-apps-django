from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("This is the index page of work00.")


def list(request):
    num = 233333 * 3333
    return HttpResponse(f"This is the list page of work00. {num}")
