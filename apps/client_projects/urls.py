from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^client/add$', views.show_add_client, name="show_add_client"),
    url(r'^client/add/add_client$', views.add_client, name="add_client"),
    url(r'^client/(?P<client_id>\d+)$', views.show_client, name="show_client"),
    url(r'^client/(?P<client_id>\d+)/add$', views.show_add_project, name="show_add_project"),
    url(r'^client/(?P<client_id>\d+)/add/add_project$', views.add_project, name="add_project"),
    url(r'^client/(?P<client_id>\d+)/project/(?P<project_id>\d+)$', views.show_project, name="show_project"),
]
