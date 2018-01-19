from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^wish_items/create$', views.create, name='create'),
    url(r'^wish_items/add$', views.add, name='add'),
    url(r'^wish_items/(?P<item_id>\d+)$', views.display, name='display'),
    url(r'^wish_items/(?P<item_id>\d+)/add$', views.item_add),
    url(r'^wish_items/(?P<item_id>\d+)/remove$', views.remove),
    url(r'^wish_items/(?P<item_id>\d+)/delete$', views.delete),
]