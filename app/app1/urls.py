from django.conf.urls import url
from app.app1 import views

urlpatterns = [
    url(r'^$', views.Model1List.as_view(), name='model1')
]
