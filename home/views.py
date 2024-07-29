from django.shortcuts import render, redirect
from home.models import HomePage, ScreenFrame, MobileMockup
from .forms import WebOrderForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from product.models import Product
from django.utils import translation


def homePage(request):
    lang = request.GET.get("lang", "az")  # Default to 'az'

    translation.activate(lang)
    request.session["_language"] = lang
    home_page = HomePage.objects.first()
    screen_frames = ScreenFrame.objects.all()
    mobile_mockups = MobileMockup.objects.all()
    products = Product.objects.all()
    context = {
        "home_page": home_page,
        "screen_frames": screen_frames,
        "mobile_mockups": mobile_mockups,
        "products": products,
    }

    if request.method == "POST":
        form = WebOrderForm(request.POST)
        if form.is_valid():
            form.save()
            context["success_message"] = "Order submitted successfully!"
        else:
            context["error_message"] = "An error occurred while sending the order."

    return render(request, "index.html", context)
