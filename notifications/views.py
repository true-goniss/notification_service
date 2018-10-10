from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from notifications.forms import *
from home.models import selectedItems
from django.conf import settings
import urllib
import urllib.request
import requests

from django.core.cache import cache
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_staff)
def email(request):
    if request.method == 'GET':

        form = ContactForm(initial={'from_email': settings.EMAIL_HOST_USER},)

    else:
        site_email = settings.EMAIL_HOST_USER

        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']

            message = form.cleaned_data['message']

            selected_items = cache.get('selected_items')



            try:
                for item in selected_items:
                    to_email = [site_email, item.email]
                    send_mail(subject, message, settings.EMAIL_HOST_USER, to_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "notifications/email.html", {'form': form})

@user_passes_test(lambda u: u.is_staff)
def whatsapp(request):
    if request.method == 'GET':
        form = ContactForm(initial={'from_email': settings.TWILIO_NUMBER},)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            selected_items = cache.get('selected_items')

            try:
                for item in selected_items:

                    message_data = {
                        "To": "whatsapp:" + item.phone,
                        "From": settings.TWILIO_NUMBER,
                        "Body": subject + ": \n" + message,
                    }
                response = requests.post(settings.TWILIO_MESSAGE_ENDPOINT, data=message_data,auth=(settings.TWILIO_SID, settings.TWILIO_AUTHTOKEN))

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "notifications/whatsapp.html", {'form': form})

def thanks(request):
    return HttpResponse('Оповещение отправлено.')
