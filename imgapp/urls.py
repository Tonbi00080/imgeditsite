from django.urls import path
from . import views

app_name = 'imgapp'
urlpatterns = [
    path('', views.index,name='index'),
]
