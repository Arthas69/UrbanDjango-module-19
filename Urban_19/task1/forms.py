from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, required=True, label="Введите логин")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Введите пароль", required=True)
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Повторите пароль", required=True)
    age = forms.IntegerField(label="Введите свой возраст")