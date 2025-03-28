
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


class RegisterView(APIView):
    # 注册
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):
    # 登录
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh)
                })
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeView(APIView):
    # 个人中心
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
        return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)