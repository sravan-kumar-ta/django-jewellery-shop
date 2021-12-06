from django.urls import reverse
from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=60, verbose_name="Category Title")
    slug = models.SlugField(max_length=60, verbose_name="Category Slug")
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('category-products', args=[self.slug])


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name="Product Title")
    slug = models.SlugField(max_length=160, verbose_name="Product Slug")
    desc = models.TextField(verbose_name="Product Description")
    product_image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name="Product Image",
                                      default="products/default_image.img")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name="Product Category", on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="Is Active?")

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("product-detail", args=[self.category.slug, self.slug])
