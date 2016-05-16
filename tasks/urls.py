from django.conf.urls import url
from tasks import views

urlpatterns = [
    url(r'^tasks/$', views.card_list),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.card_detail)
    ]
