from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_image')
    description = models.TextField()
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.price}"