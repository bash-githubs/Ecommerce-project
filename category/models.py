from django.urls import reverse
from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    description=models.TextField(max_length=255, blank=True)
    cat_image=models.ImageField(upload_to='media/categories', blank=True)
    

    class Meta:
        verbose_name_plural='categories'

    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self) -> str:
        return self.category_name



        