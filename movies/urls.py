from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
]
