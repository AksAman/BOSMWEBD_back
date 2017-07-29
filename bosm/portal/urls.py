from django.conf.urls import url
from . import views


app_name = 'portal'

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^register_events/$', views.eveRegister, name='E_Register'),
    url(r'^upload/$', views.Result.as_view(), name='uploadResult'),
    url(r'^details/$', views.detail, name='detail'),
    url(r'^add_event/$', views.EventCreate.as_view(), name='add_event'),
]