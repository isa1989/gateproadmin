from django.shortcuts import render
from home.models import HomePage, ScreenFrame, MobileMockup


def homePage(request):
    home_page = HomePage.objects.first()
    screen_frames = ScreenFrame.objects.all()
    mobile_mockups = MobileMockup.objects.all()
    context = {
        "home_page": home_page,
        "screen_frames": screen_frames,
        "mobile_mockups": mobile_mockups,
    }

    return render(request, "index.html", context)
