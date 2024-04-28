from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductAPI.as_view(), name='product_list'),
    path('req/', views.RequestAPI.as_view(), name='request'),
    path('req2/', views.RequestAPI2.as_view(), name='request2'),
]

