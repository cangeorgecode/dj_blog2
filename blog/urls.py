from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('readblog/<article_id>/', views.readblog, name='readblog'),
]