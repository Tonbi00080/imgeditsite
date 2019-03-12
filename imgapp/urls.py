from django.urls import path
from . import views

app_name = 'imgapp'
urlpatterns = [
    path('', views.index,name='index'),
    path('upload/', views.upload,name='upload'),
    path('preview', views.preview,name='preview'),
    path('complete', views.complete,name='complete')
]
