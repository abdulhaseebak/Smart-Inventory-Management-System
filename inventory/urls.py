from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet,
    SupplierViewSet,
    PurchaseViewSet,
    SaleViewSet,
    dashboard
)

router = DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('', dashboard, name='dashboard'),
]

urlpatterns += router.urls