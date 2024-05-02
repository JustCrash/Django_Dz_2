from django.urls import path

from catalog.views import HomeListView, ContactsView, ProductDetailView

urlpatterns = [
    path('', HomeListView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]
