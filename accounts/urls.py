from django.urls import path
from . import views

app_name = 'accuonts'


urlpatterns = [
    path('',views.Memmber.as_view(),name='account')

]
