from django.urls import path
from . import views
from mysite.urls import urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    ]