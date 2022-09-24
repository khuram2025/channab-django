from http.client import HTTPResponse
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

from accounts.forms import UserForm

# Create your views here.


def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store")

    else:
        form = UserForm()
    context = {
        'form' : form
    }
    return render(request, 'account/registeruser.html', context)