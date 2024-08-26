from django.contrib import admin
from django.urls import path
from . import views
app_name = "order"
urlpatterns = [

    path('',views.Orders.as_view(),name='order'),
    path("accounts/<str:name>", views.Name_order.as_view()),
    path('order/<str:order>', views.Orders.as_view(), name='orders'),




]
