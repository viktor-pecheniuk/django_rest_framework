from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import User


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    nickname = serializers.CharField(max_length=100)


class GroupSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=100)