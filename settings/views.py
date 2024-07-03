from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PlayStoreForm


def playstore_form(request):
    if request.method == "POST":
        form = PlayStoreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/settings/form-submitted/")
    else:
        form = PlayStoreForm()

    return render(request, "settings/playstore_form.html", {"form": form})


def form_submitted(request):
    return render(request, "settings/form_submitted.html")
