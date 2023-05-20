from rest_framework import viewsets
from api.product.models import Product
from api.product.serializers import ProductSerializer
from api.utils.permission import IsTAdmin
from api.utils.renderers import CustomeJSONRenderer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = (CustomeJSONRenderer,)
    permission_classes = (IsTAdmin,)
