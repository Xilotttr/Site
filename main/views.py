from django.shortcuts import render


def index(request):
    data = {
        'title': 'Homepage',
        'header': 'Welcome'
    }
    return render(request, 'main/index.html', data)


def profile(request):
    data = {
        'title': 'Account'
    }
    return render(request, 'main/profile.html', data)


def settings(request):
    data = {
        'title': 'Settings'
    }
    return render(request, 'main/settings.html', data)




