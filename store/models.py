import uuid
from django.db import models
from django.urls import reverse
from category.models import Category

class Product(models.Model):
    product_name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)
    product_description=models.CharField(max_length=255, null=True, blank=True)
    price=models.IntegerField()
    images=models.ImageField(upload_to='media/photos')
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    

    def __str__(self) -> str:
        return self.product_name