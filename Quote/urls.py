from django.conf.urls import patterns, include, url
from django.contrib import admin

from quotes import views

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^$', views.login_user, name='login_user'),
                       url(r'^logout_user/$', views.logout_user, name='logout_user'),
                       url(r'^index/$', views.index, name='index'),
                       url(r'^add_quote/$', views.add_quote, name='add_quote'),
                       url(r'^quote/$', views.quote, name='quote'),
                       )
