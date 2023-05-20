from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.account.models import User

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email","password"]
        extra_kwargs = {'password' : {'write_only': True},}

    def create(self, validated_data):
        member = User.objects.create(email=validated_data['email'])
        member.set_password(validated_data['password'])
        member.save()
        return member

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    default_error_messages = {
        "no_active_account": ["Bad Request","No active account found with the given credentials"]
    }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'],token['user_role'] = user.email,user.user_role
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user_role'] = str(self.user.user_role)
        return data