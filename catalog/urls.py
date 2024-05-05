from django.urls import path

from catalog.views import (
    HomeListView,
    ContactsView,
    ProductDetailView,
    BlogPostDetailView,
    BlogPostListView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeListView.as_view(), name="product_list_basic"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/", BlogPostListView.as_view(), name="blogpost_list"),
    path("blogpost/create/", BlogPostCreateView.as_view(), name="blogpost_from"),
    path("blogpost/<int:pk>/", BlogPostDetailView.as_view(), name="blogpost_detail"),
    path(
        "blogpost/<int:pk>/update/",
        BlogPostUpdateView.as_view(),
        name="blogpost_update",
    ),
    path(
        "blogpost/<int:pk>/delete/",
        BlogPostDeleteView.as_view(),
        name="blogpost_delete",
    ),
]
