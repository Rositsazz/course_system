from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name="index_name"),
    url(r'^index/fact/$', views.fact, name="fact_name"),
    url(r'^index/fib/$', views.fib, name="fib_name"),
    url(r'^index/prime/$', views.prime, name="prime_name"),
]
