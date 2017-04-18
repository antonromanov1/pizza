from django.conf.urls import url

import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^pizza$', views.pizza, name='pizza'),
    url(r'^hot$', views.hot, name='hot'),
    url(r'^salads$', views.salads, name='salads'),
    url(r'^drinks$', views.drinks, name='drinks'),
    url(r'^desserts$', views.desserts, name='desserts'),
    url(r'^order$', views.order, name='order'),
    url(r'^address$',  views.address,  name='address'),
    url(r'^akcii$',  views.akcii,  name='akcii'),
    url(r'^staff$',  views.staff,  name='staff'),
    url(r'^howto$',  views.howto,  name='howto')
]
