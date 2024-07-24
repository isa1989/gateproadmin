from django.shortcuts import render, redirect
from .forms import WebOrderForm


def create_order(request):
    if request.method == "POST":
        form = WebOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_success")  # Redirect to a success page
    else:
        form = WebOrderForm()
    return render(request, "create_order.html", {"form": form})
