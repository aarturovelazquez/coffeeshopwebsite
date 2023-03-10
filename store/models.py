from django.db import models

class User(models.Model):
    user_fullname = models.CharField(max_length=100)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=16)

    def __str__(self):
        return self.user_fullname
        return self.user_email
        return self.user_password

class Orders(models.Model):
    order_email = models.CharField(max_length=100)
    order_firstname  = models.CharField(max_length=100)
    order_lastname  = models.CharField(max_length=100)
    order_email  = models.CharField(max_length=100)
    order_address  = models.CharField(max_length=200)
    order_country  = models.CharField(max_length=200)
    order_city  = models.CharField(max_length=200)
    order_zip  = models.CharField(max_length=6)
    order_products = models.CharField(max_length=500)

    def __str__(self):
        return self.order_email
        return self.order_firstname
        return self.order_lastname
        return self.order_email
        return self.order_address
        return self.order_country
        return self.order_city
        return self.order_zip
        return self.order_products

    