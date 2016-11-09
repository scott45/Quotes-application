from django.conf.urls import patterns, include, url
from django.contrib import admin
from quotes import views

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^quote/add/$', views.QuoteCreate.as_view(), name='quote-add'),
                       url(r'^quote/(?P<pk>[0-9]+)/$', views.QuoteUpdate.as_view(), name='quote-update'),
                       url(r'^quote/(?P<pk>[0-9]+)/delete/$', views.QuoteDelete.as_view(), name='quote-delete'),
                       )
