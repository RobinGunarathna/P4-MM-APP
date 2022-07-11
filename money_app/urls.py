from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "money_app")
    path('add-money_app', views.add_mapp, name = 'add-money_app')
]