from django.shortcuts import render


def index(request):
    # reiwa.htmlを表示する
    return render(request, "work06/reiwa.html")
