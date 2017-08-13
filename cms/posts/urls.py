from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^(?P<cname>\w+)/$', views.post_list, name='category_post_list'),
	url(r'^(?P<cname>\w+)/(?P<pname>[-\w]+)$', views.post_detail, name='post_detail'),
	url(r'^search$', views.search, name='search'),
	]