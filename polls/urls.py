from django.urls import path
from django.urls import include
from django.conf.urls import url
from .  import  views
app_name='polls'
urlpatterns = [
     url(r'^$',views.index,name='index'),
     url(r'^(?P<qustion_id>[0-9]+)/$',views.detail,name='detail'),
     url(r'^(?P<qustion_id>[0-9]+)/results/$',views.results,name='results'),
     url(r'^(?P<qustion_id>[0-9]+)/vote/$',views.vote,name='vote'),
]