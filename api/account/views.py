from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from api.account.models import User
from api.account.serializers import CreateUserSerializer, MyTokenObtainPairSerializer
from api.utils.renderers import CustomeJSONRenderer

# Create your views here.

class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    renderer_classes = (CustomeJSONRenderer,)

    def post(self, request, *args, **kwargs):
        user_role = self.request.path.split('/')[-2]
        serializer = CreateUserSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                member=User.objects.get(email=(serializer.data)["email"])
                member.user_role = "Customer" if user_role == "customer" else "TAdmin"
                member.save()
                return Response('User Created Successfully',status=status.HTTP_201_CREATED)
        except:
            return Response('User with email already exits',status=status.HTTP_403_FORBIDDEN)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    renderer_classes = (CustomeJSONRenderer,)