from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^index/fact/$', views.fact, name="fact"),
    url(r'^index/fib/$', views.fib, name="fib"),
    url(r'^index/prime/$', views.prime, name="prime"),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^profile$', views.home, name='profile'),
    url(r'^logout$', views.logout, name='logout'),
]
