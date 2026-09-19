from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from django.contrib.auth.models import User

from api import serializers
from api import models

### Users CRUD
#List
class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        data = serializers.UserSerializerList(users, many=True).data
        return Response(data)

#detail
class UserDetailAPIView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        data = serializers.UserSerializerDetail(user).data
        return Response(data)


### Banks CRUD

#create
class createUserApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    #llamado al serializador
    serializer_class = serializers.CreateUserSerializer

#retrieve

#list
class BankListAPIView(APIView):
    def get(self, request):
        banks = models.Bank.objects.all()
        data = serializers.BankSerializerList(banks, many=True).data
        return Response(data)


#detail
class BankDetailAPIView(APIView):
    def get(self, request, pk):
        bank = models.Bank.objects.get(pk=pk)
        data = serializers.BankSerializerDetail(bank, many=False).data
        return Response(data)
    
#update

#delete

### Accounts CRUD
class AccountListAPIView(APIView):
    def get(self, request):
        accounts = models.Account.objects.all()
        data = serializers.AccountSerializerList(accounts, many=True).data
        return Response(data)

class AccountDetailAPIView(APIView):
    def get(self, request, pk):
        account = models.Account.objects.get(pk=pk)
        data = serializers.AccountSerializerDetail(account).data
        return Response(data)