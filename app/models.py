from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='image/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
