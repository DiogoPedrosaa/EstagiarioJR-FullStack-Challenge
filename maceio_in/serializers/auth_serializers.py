from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
import re

User = get_user_model() 




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("As senhas não coincidem, verifique letras maiúsculas, números, etc...")

        password = data['password']
        if len(password) < 8:
            raise serializers.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        if not re.search(r'[A-Z]', password):
            raise serializers.ValidationError("A senha deve conter pelo menos uma letra maiúscula.")

        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm') 
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()

        if user and user.check_password(data['password']):
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        raise serializers.ValidationError("Credenciais não encontradas")