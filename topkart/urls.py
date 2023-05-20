from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('api.account.urls')),
    path('product/', include('api.product.urls')),
    path('order/', include('api.order.urls')),
]
