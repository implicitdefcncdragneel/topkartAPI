from django.utils import timezone
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.order.models import Order
from api.order.serializers import LightningDealSerializer, OrderApprovalSerializer, OrderSerializer, OrderStatusSerializer
from api.product.models import LightningDeal
from api.utils.permission import IsTAdmin
from api.utils.renderers import CustomeJSONRenderer

# Create your views here.

class LightningDealListView(generics.ListAPIView):
    queryset = LightningDeal.objects.filter(expiry_time__gte=timezone.now())
    serializer_class = LightningDealSerializer
    permission_classes = [IsAuthenticated,]
    renderer_classes = (CustomeJSONRenderer,)

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]
    renderer_classes = (CustomeJSONRenderer,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['product_id'] = self.kwargs['product_id']
        return context
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response("Order Placed Successfully", status=status.HTTP_201_CREATED)
    
class OrderStatusView(generics.RetrieveAPIView):
    serializer_class = OrderStatusSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (CustomeJSONRenderer,)
    lookup_field = "id"

    def get(self, request, *args, **kwargs):

        id = self.kwargs.get('id')
        if id is not None:
            return super().get(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data)

    def get_queryset(self):
        
        user = self.request.user
        queryset = Order.objects.filter(user=user)
        id = self.kwargs.get('id',None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset
    
class OrderActionView(generics.UpdateAPIView):
    serializer_class = OrderApprovalSerializer
    queryset = Order.objects.all()
    permission_classes = (IsTAdmin,)
    renderer_classes = [CustomeJSONRenderer]
    lookup_field = "id"