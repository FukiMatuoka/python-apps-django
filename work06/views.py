from django.shortcuts import render

from work06.forms import YearConvertForm


def index(request):
    # YearConvertFormフォームを使って令和から西暦へ変換するツールを作る
    # 初期化
    if request.method == "POST":
        form = YearConvertForm(request.POST)

        if form.is_valid():
            year_input = form.cleaned_data["year"]
            original_year = int(year_input)  # 仮の変換元年

            converted_year = (
                2018 + original_year
            )  # 令和元年は2019年なので、2019 - 2 = 2017を足す
        else:
            original_year = None
            converted_year = None

        template_values = {
            "form": form,
            "aisatsu": "postです",
            "original_year": original_year,
            "converted_year": converted_year,
        }

    else:

        # GETリクエストの場合、空のフォームを表示
        form = YearConvertForm()
        template_values = {
            "form": form,
            "aisatsu": "おはようございます",
        }

    # reiwa.htmlを表示する
    return render(request, "work06/reiwa.html", template_values)
