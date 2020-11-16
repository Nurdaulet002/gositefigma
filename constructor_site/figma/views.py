from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, View
from .models import Good, Category


class ClientIndexView(TemplateResponseMixin,View):
    template_name = 'figma/client-site/index.html'

    def get (self, request, category=None):
        categories = Category.objects.all()
        goods = Good.objects.filter(top=True)
        if category:
        	goods = goods.filter(category=category)
        return self.render_to_response({
        	'categories': categories, 'goods': goods})




  
