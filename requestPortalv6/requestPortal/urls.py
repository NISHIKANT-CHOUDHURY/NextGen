from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls import (
    url,
    include
)
from django.core.urlresolvers import reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from itservices.forms import LoginForm


urlpatterns = [
                  # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
                  # Examples:
                  # url(r'^$', 'karunatravels.views.home', name='home'),
                  # url(r'^blog/', include('blog.urls')),

                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^', include('itservices.urls')),
                  
                  url(r'^login/$', views.login, {'template_name': 'home/login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.logout, {'next_page': '/login'}), 
                  
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
