from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import User
import pickle

CSV_PATH = '/home/administrator/test.csv'

def data_serializer(request):
    with open('data.pickle', 'wb') as file:
        serialized_data = pickle.dump(request, file)
        print "SER >>>", serialized_data
    return serialized_data

class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    nickname = serializers.CharField(max_length=100)


class GroupSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=100)