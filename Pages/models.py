from django.db import models
class Book_Data(models.Model):
    book_id = models.AutoField(primary_key=True)   
    book_name = models.CharField(max_length=100)
    book_price = models.FloatField(default=0.0)
    book_description = models.TextField(default="")

    class Meta:
        db_table = "book"


class User_Data(models.Model):
    user_id = models.AutoField(primary_key=True) 
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=200)
    user_password = models.CharField(max_length=100)

    class Meta:
        db_table = "users"


class Cart_Data(models.Model):
    user_name = models.CharField(max_length=100)
    cart_itemId = models.AutoField(primary_key=True)
    cart_itemName = models.CharField(max_length=100)
    cart_itemPrice = models.FloatField(default=0.0)
    cart_itemDes = models.TextField(default="")

    class Meta:
        db_table = "Cart"