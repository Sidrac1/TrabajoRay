from rest_framework import serializers

from django.contrib.auth.models import User

from api import models

### Users serializers

#List
class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'username',  
            'first_name', 
            'last_name',
            'email'
        ]

#Detail
class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

### Banks serializers

#Create
class BankSerializerCreate():
    pass

##Retrieve

#List

class BankSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = [
            'id', 
            'name',  
            'status',
        ]

#Detail

class BankSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = '__all__'

#Update

class BankSerializerUpdate():
    pass

#Delete

class BankSerializerDelete():
    pass



### Accounts serializers
class AccountSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = [
            "name",
            "bank",
            "user",
            "status"
        ]

class AccountSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = "_all_"
