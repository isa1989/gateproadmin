from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PlayStoreForm
from django.shortcuts import render, redirect
from .models import PrivacyPolicy, TermsConditions


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


def privacy_policy_view(request):
    privacy_policy = PrivacyPolicy.objects.first()
    return render(
        request, "settings/privacy_policy.html", {"privacy_policy": privacy_policy}
    )


def terms_conditions_view(request):
    terms_conditions = TermsConditions.objects.first()
    return render(
        request,
        "settings/terms_conditions.html",
        {"terms_conditions": terms_conditions},
    )
