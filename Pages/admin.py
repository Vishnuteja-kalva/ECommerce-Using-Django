from django.contrib import admin
from .models import Book_Data,User_Data,Cart_Data
# Register your models here.
@admin.register(Book_Data)

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'book_name', 'book_price', 'book_description']

@admin.register(User_Data)

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id','user_name', 'user_email', 'user_password']

@admin.register(Cart_Data)

class CartAdmin(admin.ModelAdmin):
    list_display = ['user_name','cart_itemId', 'cart_itemName', 'cart_itemPrice', 'cart_itemDes']
