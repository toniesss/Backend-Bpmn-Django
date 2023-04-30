from .serializers import Userserializer,UserLoginSerializer,UserListserializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,AllowAny
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class UserListView(APIView):
    serializer_class = UserListserializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role != 1:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            users = User.objects.all()
            serializer = self.serializer_class(users, many=True)
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Successfully fetched users',
                'users': serializer.data

            }
            return Response(response, status=status.HTTP_200_OK)


# class AuthUserLoginView(APIView):
#     serializer_class = UserLoginSerializer
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)

      

#         if valid:
#             status_code = status.HTTP_200_OK

#             response = {
#                 'success': True,
#                 'statusCode': status_code,
#                 'message': 'User logged in successfully',
#                 'authTokens': {
#                     'access': serializer.data['access'],
#                     'refresh': serializer.data['refresh'],
#                 },
#                 'authenticatedUser': {
#                     'email': serializer.data['email'],
#                     'role': serializer.data['role'],
#                     'first_name': serializer.data['first_name'],
#                     'last_name': serializer.data['last_name']
#                 }
#             }

#             return Response(response, status=status_code)


class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=serializer.validated_data['email'])
        token = RefreshToken.for_user(user)

        # Add custom claims to the token
        token['role'] = user.role
        token['firstname'] = user.first_name
        token['lastname'] = user.last_name
        token['email'] = user.email
        token['id'] = str(user.uid)
        
        # ...

        status_code = status.HTTP_200_OK

        response = {
            'message': 'User logged in successfully',
            'authTokens': {
                'access': str(token.access_token),
                'refresh': str(token),
            },
        }

        return Response(response, status=status_code)