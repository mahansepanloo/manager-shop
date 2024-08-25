from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("prodact.urls",namespace='home')),
    path('order/', include("order.urls", namespace='order')),

]
