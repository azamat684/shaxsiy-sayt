from django.urls import path
from .views import index,about,contact,hero,resume,services,portfolio,portfolio_details
urlpatterns =[
    path('',index,name='index'),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('hero/',hero,name="hero"),
    path('resume/',resume,name="resume"),
    path('portfolio/',portfolio,name="portfolio"),
    path('services/',services,name='services'),
    path('portfolio-details/',portfolio_details,name="portfolio-details")
]