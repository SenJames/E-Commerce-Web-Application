from django.db import models

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(
        verbose_name='category name', max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255)
    cat_image = models.ImageField(
        upload_to='photos/categories', verbose_name='Category Image', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True),
    slug = models.SlugField(max_length=100, unique=True),
    description = models.TextField(max_length=500, blank=True),
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name
