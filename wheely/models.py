from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])


    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Sub-Categories'
        
    def __str__(self):
        return self.name

class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory,related_name='product', on_delete=models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    color = models.ManyToManyField('Color')
    size = models.ManyToManyField('Size')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')


class Size(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.name

# class Skaters(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     city = models.CharField(max_length=255)
#     height = models.FloatField(max_digits=1, decimal_places=2)
#     weight = models.IntegerField()
#     stance = models.CharField(max_length=255)
#     style = models.CharField(max_length=255)
#     time_skating = models.IntegerField()
#     fav_park = models.CharField(max_length=255)