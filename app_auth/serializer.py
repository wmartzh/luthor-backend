from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, data):
        user = User.objects.create(
            username=data['username'], email=data['email'])
        user.set_password(data['password'])
        user.save()
        return user
