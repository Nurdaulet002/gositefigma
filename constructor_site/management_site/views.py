from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DemandForm, UserRegistrationForm
from .models import Site, UserSite, Category


# Информационная страница сайта
class InformationView(TemplateResponseMixin, View):
    template_name = 'management/information.html'

    def get(self,request):
        demand_form = DemandForm()
        return self.render_to_response({'demand_form': demand_form})

    def post(self, request):
        demand_form = DemandForm(request.POST)
        if demand_form.is_valid():
            demand_form.save()
            messages.add_message(request, messages.SUCCESS, 'Ваша заявка отправлена успешна')
            return redirect('management:information_page')
        return self.render_to_response({'demand_form': demand_form})


# Регистрация пользователя
class UserRegistrationView(TemplateResponseMixin, View):
    template_name = 'registration/registration.html'

    def get(self,request):
        registration_form = UserRegistrationForm()
        return self.render_to_response(
            {'registration_form': registration_form})

    def post(self, request):
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            new_user=registration_form.save(commit=False)
            new_user.set_password(
                registration_form.cleaned_data['password']
            )
            new_user.save()
            authenticate_user = authenticate(
                username=registration_form.cleaned_data['username'],
                password=registration_form.cleaned_data['password']
            )
            login(request, authenticate_user)
            return redirect('management:mysite_page')
        return self.render_to_response(
            {'registration_form': registration_form})    


class UserSiteCreateView(View):

    def get (self, request, site):
        user = request.user
        site = get_object_or_404(Site, id=site)
        site_user = UserSite.objects.create(site=site, user=user)
        url_address_format = 'sites' + str(site_user.id)
        site_user.url_address = url_address_format
        site_user.save()
        return redirect(site.admin_url, user_site = url_address_format)


class MySiteListView(ListView, LoginRequiredMixin):
    template_name = 'management/mysite.html'
    model = UserSite
    context_object_name = 'mysites'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class SiteListView(ListView, LoginRequiredMixin):
    template_name = 'management/site_list.html'
    model = Site
    context_object_name = 'sites'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        category = self.kwargs.get('category', None)
        if category:
            qs = qs.filter(category=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context





