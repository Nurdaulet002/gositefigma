from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib import messages
from .forms import DemandForm
from .models import Good, Category, UnderCategory, AdditionalData, Comment
from mini_crm.models import Order
from .forms import CommentForm, CategoryForm, GoodForm, SubcategoryForm
import datetime
from management_site.models import UserSite


class ClientIndexView(TemplateResponseMixin,View):
    template_name = 'clothes/client-site/information.html'

    def dispatch(self, *args, **kwargs):
        self.user_site = self.kwargs.get('user_site', None)
        self.categories = Category.objects.filter(
            user_site__url_address=self.user_site)
        self.goods = Good.objects.filter(
            is_top=True, user_site__url_address=self.user_site)
        return super().dispatch(*args, **kwargs)

    def get (self, request, *args, **kwargs):
        demand_form = DemandForm()
        return self.render_to_response({
            'categories': self.categories,
            'goods': self.goods, 'demand_form': demand_form})

    def post(self, request):
        demand_form = DemandForm(request.POST)
        if demand_form.is_valid():
            demand_form.save()
            messages.add_message(request, messages.SUCCESS, 'Ваша заявка отправлена успешна')
            return redirect('clothes:index', user_site=self.user_site)
        return self.render_to_response({
            'categories': self.categories,
            'goods': self.goods, 'demand_form': demand_form})


class GoodListView(TemplateResponseMixin,View):
    template_name = 'clothes/client-site/good_list.html'

    def get (self, request, category=None, subcategory=None):
        undercategories = None
        list_goods = Good.objects.filter(is_top=True)
        categories = Category.objects.all()
        if category:
            goods = Good.objects.filter(is_top=True)
            undercategories = UnderCategory.objects.filter(category=category)
        if subcategory:
            goods = Good.objects.filter(undercategory=subcategory)
        return self.render_to_response({
            'categories': categories, 'undercategories': undercategories,
            'goods': goods, 'category': category, 'list_goods': list_goods})


class DetailView(TemplateResponseMixin,View):
    template_name = 'clothes/client-site/detail.html'

    def get(self, request, good):
        categories = Category.objects.all()
        good = Good.objects.get(id=good)
        goods = Good.objects.filter(is_top=True)
        coment_form = CommentForm()
        coments = Comment.objects.filter()
        date = datetime.datetime.now()
        return self.render_to_response({'good': good, 'goods': goods,
            'coment_form': coment_form, 'coments':coments, 'date':date, 'categories': categories})

    def post(self, request, good):
        coment_form = CommentForm(request.POST)
        if coment_form.is_valid():
           coment_form.save()
           return redirect('clothes:detail', good=good)
        return self.render_to_response({'coment_form': coment_form})
        

class AddBagView(View):
    def get(self, request, good):
        good_obj = Good.objects.get(id=good)
        order = Order.objects.create(base_object=good_obj)
        return redirect('clothes:detail', good=good)


class ConstructIndexView(TemplateResponseMixin,View):
    template_name = 'clothes/constructor-site/information.html'

    def get(self, request, user_site, category=None):
        category_form = CategoryForm()
        good_form = GoodForm()
        categories = Category.objects.filter(user_site__url_address=user_site)
        goods = Good.objects.filter(is_top=True, user_site__url_address=user_site)
        return self.render_to_response(
            {'categories': categories, 'goods': goods, 
            'category_form': category_form, 'good_form': good_form, 'user_site': user_site}
        )



class CategoryCreateView(View):

    def get(self, request, user_site):
        user_site_base = UserSite.objects.get(url_address=user_site)
        category_obj = Category.objects.get(id=47)
        category_obj.pk = None
        category_obj.user_site = user_site_base
        category_obj.save()
        return redirect('clothes:creat_index', user_site=user_site)



class GoodCreateView(View):

    def get(self, request, user_site, subcategory=None):
        user_site_base = UserSite.objects.get(url_address=user_site)
        good_obj = Good.objects.get(id=80)
        good_obj.pk = None
        good_obj.user_site = user_site_base
        good_obj.save()
        return redirect('clothes:creat_index', user_site=user_site)
        

class CreatGoodListView(TemplateResponseMixin,View):
    template_name = 'clothes/constructor-site/good/list.html'

    def get(self, request, category=None, subcategory=None, user_site=None):
        subcategory_form = SubcategoryForm()
        undercategories = None
        list_goods = Good.objects.filter(is_top=True, user_site__url_address=user_site)
        categories = Category.objects.filter(user_site__url_address=user_site)
        if category:
            goods = Good.objects.filter(is_top=True, user_site__url_address=user_site)
            undercategories = UnderCategory.objects.filter(category=category, user_site__url_address=user_site)
        if subcategory:
            goods = Good.objects.filter(undercategory=subcategory, user_site__url_address=user_site)
        return self.render_to_response({
            'categories': categories, 'undercategories': undercategories,
            'goods': goods, 'category': category, 'list_goods': list_goods, 'user_site': user_site, 'subcategory_form': subcategory_form})


class SubcategoryCreateView(View):

    def post(self, request, user_site, category):
        category_obj = Category.objects.get(id=category)
        user_site_base = UserSite.objects.get(url_address=user_site)
        subcategory_form = SubcategoryForm(request.POST)
        if subcategory_form.is_valid():
            obj_save = subcategory_form.save(commit=False)
            obj_save.user_site = user_site_base
            obj_save.category = category_obj
            obj_save.save()
            return redirect('clothes:creat_good_list', category=category,  user_site=user_site)


class UpdateTitleGoodView(View):

    def get(self, request, user_site):
        id = request.GET.get('id')
        type = request.GET.get('type')
        text = request.GET.get('text', None)
        good = Good.objects.get(id=id)
        if type=='title':
            good.title = text
        if type=='price':
            good.price = text
        good.save()
        return HttpResponse('izmenen')


class UpdateOrCreateAdditionalDataView(View):

    def get(self, request, user_site):
        user_site_base = UserSite.objects.get(url_address=user_site)
        element_id = request.GET.get('element_id')
        type = request.GET.get('type')
        text = request.GET.get('text', None)
        obj, create = AdditionalData.objects.get_or_create(
            element_id = element_id,
            user_site = user_site_base,
            defaults = {'label':text}
            )
        if not create:
            if type=='label':
                obj.label = text
            obj.save()
        return HttpResponse('izmenen')


class UpdateCategoryView(View):

    def get(self, request, user_site):
        id = request.GET.get('id')
        text = request.GET.get('text')
        Category.objects.filter(id=id).update(title=text)
        return HttpResponse('izmenen')


class DeleteCategoryView(View):

    def get(self, request, user_site):
        id = request.GET.get('id')
        Category.objects.filter(id=id).delete()
        return HttpResponse('deleted')

class DeleteGoodView(View):

    def get(self, request, user_site):
        id = request.GET.get('id')
        Good.objects.filter(id=id).delete()
        return HttpResponse('deleted')
