from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from .views import CartViewSet, CartItemViewSet  

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"carts", CartViewSet, basename="carts")
router.register(r"cart-items", CartItemViewSet, basename="cart-items")

urlpatterns = [
    path("", include(router.urls))
]