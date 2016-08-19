from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registerprocess$', views.registerprocess),
    url(r'^signinprocess$', views.signinprocess),
    url(r'^travels', views.travels),
    url(r'^add$', views.add),
    url(r'^processadd$', views.processadd),
    url(r'^logout$', views.logout),
]
