from django.conf.urls import url
from . import views

from .views import (
    ComponyListAPIView,
    ClientListAPIView,
    UserListAPIView,
    
    
    ComponyCreateAPIView,
    UserCreateAPIView,
    ClientCreateAPIView,
    
    

    ComponyADetailAPIView,
    UserADetailAPIView,
    


    UserDeleteAPIView,
    ComponyDeleteAPIView,

)


urlpatterns = [
    
    url(r'^$', views.home, name='home'),

    url(r'^user/$', UserListAPIView.as_view(), name='get'),
    url(r'^client/$', ComponyListAPIView.as_view(), name='get'),
    

    url(r'^compony/$', ClientListAPIView.as_view(), name='get'),
    
    
    


   
    url(r'^create/client/api/$', ClientCreateAPIView.as_view(), name='post'),


    url(r'^signup/$', UserCreateAPIView.as_view(), name='post'),
    url(r'^client/new/$', ComponyCreateAPIView.as_view(), name='post'),
    

    
    url(r'^client/(?P<pk>\d+)/$', ComponyADetailAPIView.as_view(), name='put'),
    url(r'^user/(?P<pk>\d+)/$', UserADetailAPIView.as_view(), name='put'),
    


    url(r'^user/(?P<pk>\d+)/$', UserDeleteAPIView.as_view(), name='delete'),
    url(r'^client/(?P<pk>\d+)/$',
        ComponyDeleteAPIView.as_view(), name='delete'),

]
