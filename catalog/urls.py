from django.urls import path

from catalog.views import home, contacts, product_detail

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('product/<int:pk>/', product_detail)
]
