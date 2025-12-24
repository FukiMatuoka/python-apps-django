# forms.py
from django import forms


class YearConvertForm(forms.Form):
    year = forms.IntegerField(
        label="年を入力してください（例：令和年、2021年）",
        required=True,
    )
