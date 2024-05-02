from django.urls import path

from catalog.views import HomeListView, contacts, ProductDetailView

urlpatterns = [
    path('', HomeListView.as_view()),
    path('contacts/', contacts),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]
