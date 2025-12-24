from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from datetime import datetime
from zoneinfo import ZoneInfo


def index(request):
    datetime_now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
    return render(request, "work05/index.html", {"datetime_now": datetime_now})


def list(request):
    return HttpResponse("Hello, world. You're at the work05 list.")


def fuki(request):
    return HttpResponse("Hello,")


def kadai(request):
    return HttpResponse("Hello, world. You're at the work05 list.")
