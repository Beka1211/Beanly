from django.urls import path
from .views import (
    IndexView,
    CategoryView,
    ProductListView,
    ProductDetailView,
    BrandListView,
    ReviewListCreateView,
    ReviewDetailView
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("categories/", CategoryView.as_view(), name="categories"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("brands/", BrandListView.as_view(), name="brand-list"),
    path("reviews/", ReviewListCreateView.as_view(), name="review-list"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
]
