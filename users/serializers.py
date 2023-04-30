from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.auth import authenticate


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid','email','first_name',"last_name","username","role"]

class UserListserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'       

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

    # def create(self, validated_date):
    #     pass

    # def update(self, instance, validated_data):
    #     pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            # update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'password': user.password,
                'role': user.role,
                'first_name' : user.first_name,
                "last_name" : user.last_name
            }

            return validation
        # except AuthUser.DoesNotExist:
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")        