from django.db import models
from management_site.models import UserSite
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Order(models.Model):
    user_site = models.ForeignKey(UserSite, on_delete=models.CASCADE, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    base_object = GenericForeignKey('content_type', 'object_id')
    counter = models.IntegerField(null=True)
    size =  models.CharField(max_length=4, null=True)
    client_name = models.CharField(max_length=15, null=True)
    phone = models.CharField(max_length=11, null=True)
    is_payed = models.BooleanField(default=False, null=True) 
