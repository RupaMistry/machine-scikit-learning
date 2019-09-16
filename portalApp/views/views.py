
from django.shortcuts import render, redirect
from portalApp.mongo import BaseModel


def home(request):
    return render(request, "home.html")


def about_us(request):
    if request.method == 'GET':
        return render(request, 'about_us.html', context=None)

def dashboard(request):
    if request.method == 'GET':
        user_id = request.user.id
        mongo_models = BaseModel.objects(user_id=user_id)
        context = dict(
            my_models=mongo_models
        )
        return render(request, 'dashboard.html', context)

