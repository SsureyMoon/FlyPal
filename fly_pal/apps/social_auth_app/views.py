from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from social.backends.utils import load_backends
from django.conf import settings


# Create your views here.
def main(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect("/flights")

    return render(request, 'pages/main.html',
                  {"user": request.user, 'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)})

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/flights")
    return render(request, 'pages/login.html',
                  {"user": request.user, 'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")