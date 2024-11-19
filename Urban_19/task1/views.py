import os

from django.shortcuts import render
from secrets import compare_digest

from .forms import UserRegister
from .models import Buyer, Game


# Create your views here.
def platform(request):
    return render(request, 'platform.html', {'pagename': 'Главная страница'})


def all_games(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'pagename': 'Игры', 'games': games})


def my_cart(request):
    cart = []
    # cart = [
    #     {"title": "Assassin's Creed", "price": 59.99},
    #     {"title": "GTA V", "price": 59.99},
    #     {"title": "DOOM 3", "price": 59.99},
    #     {"title": "Atomic Heart", "price": 59.99},
    #     {"title": "Cyberpunk 2077", "price": 59.99}
    # ]
    pagename = "Ваша корзина пуста" if not cart else "Корзина"
    return render(request, 'cart.html', {'pagename': pagename, 'cart': cart})


def sign_up_by_django(request):
    context = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            context['errors'] = []
            if not compare_digest(password, repeat_password):
                context['errors'].append('Пароли не совпадают')
            elif age < 18:
                context['errors'].append('Возраст должен быть не менее 18')
            elif Buyer.objects.all().filter(name=username):
                context['errors'].append('Пользователь уже существует')
            else:
                context['success'] = f'Hello, {username}'
                Buyer.objects.create(name=username, balance=0, age=age)

    else:
        form = UserRegister()
    context['form'] = form
    context['pagename'] = "Регистрация"

    return render(request, 'registration_page.html', context)
