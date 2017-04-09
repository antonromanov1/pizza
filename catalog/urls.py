from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pizza$', views.pizza, name='pizza'),
    url(r'^hot$', views.pizza, name='hot'),
    url(r'^salads$', views.pizza, name='salads'),
    url(r'^drinks$', views.pizza, name='drinks'),
    url(r'^desserts$', views.pizza, name='desserts')
]
