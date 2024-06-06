from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    HomeListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
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
    path("catalog/create/", ProductCreateView.as_view(), name="product_form"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
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
