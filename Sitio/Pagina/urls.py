from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^inicio/$', views.mostrar_inicio),
]
