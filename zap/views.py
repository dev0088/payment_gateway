# Create your views here.
import json

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect


# def index(request):
#     # return HttpResponse('Hello from Python!')
#     return render(request, "index.html")

def index(request):
    return redirect(reverse("app"))
    # if request.user.is_authenticated:
    #     return redirect(reverse("app"))
    # else:
    #     return render(request, 'registration/login.html')

def home(request, *arg, **kwargs):
    return redirect(reverse("app"))
    # if request.user.is_authenticated:
    #     return redirect(reverse("app"))
    # else:
    #     return render(request, 'registration/login.html')

def app(request):
    context = {
        'permissions': json.dumps(list(request.user.get_all_permissions()))
    }

    template = 'backend/app.html'
    return render(request, template, context)

