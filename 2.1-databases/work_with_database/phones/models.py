from django.db import models


class Phone(models.Model):
    name = models.TextField()
    image = models.TextField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.TextField()

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, price: {self.price}"
