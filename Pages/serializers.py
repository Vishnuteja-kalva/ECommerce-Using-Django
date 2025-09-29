from rest_framework import serializers
from .models import Book_Data,User_Data,Cart_Data

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Data
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Data
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Data
        fields = '__all__'
