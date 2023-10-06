from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"index.html")

def hero(request):
    return render(request,"index.html")

def resume(request):
    return render(request,"index.html")

def portfolio(request):
    return render(request,"index.html")

def services(request):
    return render(request,"index.html")

def portfolio_details(request):
    return render(request,"portfolio-details.html")