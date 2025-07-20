# store/models.py
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('books', 'Books'),
        ('home', 'Home'),
        ('toys', 'Toys'),
        ('car', 'Car'),
        ('bicycle', 'Bicycle'),
        ('clothe', 'Clothe'),
        ('shoe', 'Shoe'),
        ('bag', 'Bag'),
        ('gun', 'Gun'),
        ('cap', 'Cap'),
        ('house', 'House'),
    ]

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')

    def get_discount_percentage(self):
        return int(100 - (self.discount_price / self.original_price) * 100)

    def __str__(self):
        return self.name


from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')

    def __str__(self):
        return self.user.username
