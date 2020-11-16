from django.db import models
from django.contrib.auth.models import User


# Список категории
class Category(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


# Список сайтов
class Site(models.Model):
    title = models.CharField(max_length=120)
    cost = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    is_top = models.BooleanField(default=False,null=True)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    client_url = models.CharField(max_length=120, blank=True)
    admin_url = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.title


# Списки сайтов, выбранные пользователем
class UserSite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    url_address = models.SlugField(max_length=120, unique=True)


# Список заявок
class Demand(models.Model):
    title = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.title





