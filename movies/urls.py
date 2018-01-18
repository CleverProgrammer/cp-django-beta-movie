from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('delete/<str:movie_id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('edit/<str:movie_id>', views.edit, name='edit'),
]
