from rest_framework import viewsets
from .models import Book_Data,User_Data,Cart_Data
from .serializers import BookSerializer,UserSerializer,CartSerializer

class BookViewSet(viewsets.ModelViewSet):   
    queryset = Book_Data.objects.all()
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User_Data.objects.all()
    serializer_class = UserSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart_Data.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'cart_itemId'