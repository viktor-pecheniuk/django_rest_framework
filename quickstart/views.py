from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from quickstart.models import User
from quickstart.serializers import UserSerializer, data_serializer
import csv

CSV_PATH = '/home/administrator/test.csv'

def get_csv_file(CSV_PATH):
    with open(CSV_PATH, 'rb') as file_data:
        reader = csv.DictReader(file_data)
        for row in reader:
            yield row

def write_to_csv(request):
    with open(CSV_PATH, 'a') as csvfile:
        field_names = ['id', 'name', 'nickname']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        # writer.writeheader()
        writer.writerow(request)
    return True

class UserList(APIView):
    def get(self, request, format=None):
        user = get_csv_file(CSV_PATH)
        # serializer = data_serializer(request)
        # print ">>>>", user
        return Response(user)

    def post(self, request, format=None):
        # serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer = write_to_csv(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListDetailed(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def detete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
