from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class RegisterSerializer(serializers.Serializer):
    # 邮件和密码
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, value):
        # 检查邮箱是否已存在
        if User.objects.filter(email=value).exists():
            raise ValidationError(f'{value} This email address has already been registered。')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)