import logging
from django.shortcuts import render, redirect
from django.views import View
from .utils import send_contact_info_to_telegram_chat
from django.views.generic import TemplateView
from .models import PortfolioModel
# Create your views here.
def index(request):
    return render(request,"index.html")
    

class IndexView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        try:
            send_contact_info_to_telegram_chat(request.POST)
            logging.info("Message sent successfully to Telegram")
        except Exception as e:
            logging.error(f"Error sending message to Telegram: {str(e)}")
        return render(request,"index.html")

def projects(request):
    portfolio = PortfolioModel.objects.all()
    return render(request,"portfolio.html", {'portfolios': portfolio})