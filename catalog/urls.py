from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pizza$', views.pizza, name='pizza'),
    url(r'^hot$', views.hot, name='hot'),
    url(r'^salads$', views.salads, name='salads'),
    url(r'^drinks$', views.drinks, name='drinks'),
    url(r'^desserts$', views.desserts, name='desserts'),
    url(r'^testing$', views.testing, name='testing')
]
