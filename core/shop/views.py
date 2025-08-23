from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from .models import Product, Brand, Category, Review
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer, ReviewSerializer
from .pagination import ProductPagination


class IndexView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Главная страница API: возвращает все продукты, бренды и категории",
        responses={200: "Список продуктов, брендов и категорий"}
    )
    def get(self, request):
        products = ProductSerializer(Product.objects.all(), many=True).data
        brands = BrandSerializer(Brand.objects.all(), many=True).data
        categories = CategorySerializer(Category.objects.all(), many=True).data
        return Response({
            'products': products,
            'brands': brands,
            'categories': categories
        })


class CategoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        operation_description="Получить список категорий",
        responses={200: CategorySerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand', 'is_available']

    @swagger_auto_schema(
        operation_description="Список всех продуктов или добавление нового",
        responses={200: ProductSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        operation_description="Получить, обновить или удалить конкретный продукт",
        responses={200: ProductSerializer()}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BrandListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @swagger_auto_schema(
        operation_description="Получить список брендов или создать новый",
        responses={200: BrandSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @swagger_auto_schema(
        operation_description="Получить список отзывов или создать новый",
        responses={200: ReviewSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @swagger_auto_schema(
        operation_description="Получить, обновить или удалить конкретный отзыв",
        responses={200: ReviewSerializer()}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
