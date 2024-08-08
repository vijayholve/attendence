from rest_framework import serializers
from students.models import Student
from django.contrib.auth.models import User
from base.models import orders
class serializer_restaurant(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

class User_Serializar(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email']
    /