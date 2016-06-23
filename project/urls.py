from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView

admin.autodiscover()

urlpatterns = [
    url(r'^admin$', RedirectView.as_view(url='/admin/', permanent=True)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', TemplateView.as_view(template_name='index.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^404/$', TemplateView.as_view(template_name='404.html')),
        url(r'^500/$', TemplateView.as_view(template_name='500.html')),
        url(r'^t/(.*)$', render),
    ]
