from django.urls import path
from . import views





app_name = 'home'

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('prodact/', views.Products.as_view(),name="prodact"),
    path('prodact/<str:order>', views.Products.as_view()),
    path('search=<str:searchs>',views.Search.as_view()),
    path('manager',views.ManageProduct.as_view()),
    path('manager/<str:pk>', views.Edit.as_view()),

]