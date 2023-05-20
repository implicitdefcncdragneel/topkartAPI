from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api.account.views import CreateUserAPIView, MyTokenObtainPairView

urlpatterns = [
    path('customer/',CreateUserAPIView.as_view(),name="customer"),
    path('tadmin/',CreateUserAPIView.as_view(),name="tadmin"),
    path('login/', MyTokenObtainPairView.as_view(), name='custom-token'),
    path('refresh/token/', TokenRefreshView.as_view(), name='token-refresh'),
]