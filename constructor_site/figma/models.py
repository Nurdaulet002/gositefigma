from django.db import models


# список категории
class Category(models.Model):
    title = models.CharField(max_length=30) 

    def __str__(self):
    	return self.title


# список товаров
class Good(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    top = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title			
    			