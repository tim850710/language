from django.conf.urls import url
from wiki import views


urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^$', views.wiki, name='wiki'),
    url(r'^category/(?P<categoryName>[\w\-]+)/$', views.category, name='category'),
    url(r'^addCategory/$', views.addCategory, name='addCategory'), 
]