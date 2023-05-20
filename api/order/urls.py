from django.urls import path
from api.order.views import LightningDealListView, OrderActionView, OrderCreateView, OrderStatusView

urlpatterns = [
    path('lightningdeal/',LightningDealListView.as_view(),name='lightningdeal'),
    path('<int:product_id>/', OrderCreateView.as_view(), name='place-order'),
    path('status/', OrderStatusView.as_view(), name='orders-status'),
    path('status/<int:id>/', OrderStatusView.as_view(), name='order-detail'),
    path('action/<int:id>/', OrderActionView.as_view(), name='order-Approve-Reject'),
]