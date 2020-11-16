from django.contrib import admin
from.models import Category, UnderCategory, Good, AdditionalData, Comment

admin.site.register(Category)
admin.site.register(UnderCategory)
admin.site.register(Good)
admin.site.register(AdditionalData)
admin.site.register(Comment)

# Register your models here.
