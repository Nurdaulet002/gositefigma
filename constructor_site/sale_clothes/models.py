from django.db import models
from management_site.models import UserSite


# Базовый родительский класс
class BaseMixin(models.Model):
    title = models.CharField(max_length=30)
    user_site  = models.ForeignKey(UserSite, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# Список категории
class Category(BaseMixin):
    pass


# Список подкатегории
class UnderCategory(BaseMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


# Список товаров
class Good(BaseMixin):
    is_top = models.BooleanField(default=False)
    counter = models.IntegerField(null=True)
    description = models.TextField(null=True)
    color = models.CharField(max_length=30, null=True)
    sizes = models.CharField(max_length=30, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    photo2 = models.ImageField(upload_to="images/", null=True, blank=True)
    photo3 = models.ImageField(upload_to="images/", null=True, blank=True)
    photo4 = models.ImageField(upload_to="images/", null=True, blank=True)
    undercategory = models.ForeignKey(UnderCategory, on_delete=models.CASCADE, null=True)


# Доп. данные сайта
class AdditionalData(models.Model):
    user_site  = models.ForeignKey(UserSite, on_delete=models.CASCADE, null=True)
    element_id = models.CharField(max_length=30)
    label = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.label
        

# Список заявок
class Demand(models.Model):
    title = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# Нужно удалить
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.name


