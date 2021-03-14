from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    published = models.DateField(auto_now=False, auto_now_add=False)
    picture_url = models.URLField(max_length=300)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
