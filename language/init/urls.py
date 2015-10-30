from django.conf.urls import url
from init import views

urlpatterns = [
    url(r'^$', views.init, name='init'),
]