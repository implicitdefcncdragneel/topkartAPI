from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('api.account.urls')),
    path('api/product/', include('api.product.urls')),
    path('api/order/', include('api.order.urls')),
]
