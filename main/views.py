from django.shortcuts import render
from django.views.generic import TemplateView
from main.utils import send_contact_info_to_telegram_chat
from django.shortcuts import redirect
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

class ContactView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        send_contact_info_to_telegram_chat(request.POST)
        return redirect("index.html")