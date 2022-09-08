from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class dummy(models.Model):
    id = models.IntegerField
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class Product(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title




