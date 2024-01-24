from django.shortcuts import render
from django.views.generic import TemplateView
from main.utils import send_contact_info_to_telegram_chat
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request,"index.html")


class IndexView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        print('salom')
        send_contact_info_to_telegram_chat(request.POST)
        return redirect("index.html")