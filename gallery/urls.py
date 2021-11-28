from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_image, name='search_image'),
    url(r'^location/(?P<image_location>\d+)', views.location_filter, name='location_filter'),
    url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single,name = 'single')
]