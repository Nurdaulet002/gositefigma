from django.contrib import admin
from .models import Site, UserSite, Category
admin.site.register(Site)
admin.site.register(UserSite)
admin.site.register(Category)

