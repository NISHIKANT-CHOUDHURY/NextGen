from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls import (
    url,
    include
)
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
# import views
from itservices import views

urlpatterns = [


    url(r'^dash', views.home_request, name="dash"),
    url(r'^desktop_request/', views.desktop_request, name="desktop-request"),
    url(r'^text-chat', views.text_chat, name="text-chat"),
    url(r'^audio-chat', views.audio_chat, name="audio-chat"),
    url(r'^search', views.search, name="search"),
    url(r'^submit-request', views.link_search, name="submit-request"),
    url(r'^logout/$', auth_views.logout),
# url for dummy pages
    url(r'^asset_release/', views.dummy, name="asset_release"),
    url(r'^admin_access/', views.dummy, name="admin_access"),
    url(r'^usb_access/', views.dummy, name="usb_access"),
    url(r'^dns/', views.dummy, name="dns"),
    url(r'^software_req/', views.dummy, name="software_req"),
    url(r'^network/', views.dummy, name="network"),
    url(r'^link_proposal/', views.dummy, name="link_proposal"),





    # url(r'^submit-request', views.personalization, name="submit-request"),


    url(r'^$', auth_views.login),




]
