from django.shortcuts import render

from .forms import SubscribeForm

def home(request):
    name = "gon_iss"
    current_day = "08.10.2018"

    form = SubscribeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data["name"])

        new_form = form.save()
    return render(request, 'home/home.html', locals())

