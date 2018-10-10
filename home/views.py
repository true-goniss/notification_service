from .forms import SubscribeForm
#from notifications.forms import sendEmailForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

from django.core.cache import cache
from django.contrib.auth.decorators import user_passes_test


def home(request):
    form = SubscribeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data["name"])

        new_form = form.save()
    return render(request, 'home/home.html', locals())

def email(modeladmin, request, queryset):

    selected_items = cache.get('selected_items')
    if not selected_items:
        selected_items = queryset
        cache.set('selected_items', selected_items)

    return redirect('/email/')

def whatsapp(modeladmin, request, queryset):

    selected_items = cache.get('selected_items')
    if not selected_items:
        selected_items = queryset
        cache.set('selected_items', selected_items)

    return redirect('/whatsapp/')

def thanks(request):
    return HttpResponse('Оповещение отправлено.')



def whatsapp(modeladmin, request, queryset):

    selected_items = cache.get('selected_items')
    if not selected_items:
        selected_items = queryset
        cache.set('selected_items', selected_items)

    return redirect('/whatsapp/')



