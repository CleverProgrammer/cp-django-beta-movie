from django.conf.urls import url

from .views import MovieList, MovieUpdateView, MovieDelete, MovieCreateView

urlpatterns = [
    url(r'^$', MovieList.as_view(), name='list'),
    url(r'^update/(?P<pk>[\d]+)/$', MovieUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', MovieDelete.as_view(), name='delete'),
    url(r'^add/$', MovieCreateView.as_view(), name='create'),
    ]