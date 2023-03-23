from django import forms
import datetime

class CreateTodo(forms.Form):
    title = forms.CharField(max_length=200, label='عنوان')
    sub_title = forms.CharField(max_length=100, label='درباره')
    body = forms.CharField(label='توضیحات')
    date = forms.DateTimeField(label='زمان ساختن', required=False)
