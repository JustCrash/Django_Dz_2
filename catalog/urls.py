from django.urls import path

from catalog.views import HomeListView, contacts, product_detail

urlpatterns = [
    path('', HomeListView.as_view()),
    path('contacts/', contacts),
    path('product/<int:pk>/', product_detail)
]
