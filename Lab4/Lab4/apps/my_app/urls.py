from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from Lab4.apps.my_app.views import function_view, ExampleClassBased, OrderView

urlpatterns = [
    url(r'^function_view/', function_view),
    url(r'class_based_view/', ExampleClassBased.as_view()),
    url('OrdersView/', OrderView.as_view()),
    url(r'^order/(?P<id>\d+)', OrderView.as_view(), name='order_url')
]