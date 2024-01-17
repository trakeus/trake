from django.shortcuts import render, HttpResponse

# Create your views here.
def recharge(request):
    return render(request, "recharge.html")