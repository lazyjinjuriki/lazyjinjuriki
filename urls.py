from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'), path('crush',views.crush,name='crush')
    
    ]
