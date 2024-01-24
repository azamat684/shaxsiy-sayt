from django.urls import path
from .views import IndexView, projects
urlpatterns =[
    path('', IndexView.as_view(), name='index'),
    path('portfolio', projects, name='portfolio')
]