from django.urls import path

from . import views

app_name = 'stock'
urlpatterns = [
    # ex: /stock/
    path('', views.index, name='index')
]