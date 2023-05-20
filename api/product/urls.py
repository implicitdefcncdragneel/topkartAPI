from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.product import views

router = DefaultRouter()
router.register(r'lightningdeal', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]