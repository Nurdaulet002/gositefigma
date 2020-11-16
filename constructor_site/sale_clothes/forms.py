from django import forms
from .models import Demand, Comment, Category, Good, UnderCategory


class DemandForm(forms.ModelForm):

    class Meta:
        model = Demand
        fields = ['title', 'phone']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['title']


class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['title', 'price', 'is_top', 'sizes', 'color',
            'description', 'counter', 'photo', 'photo2', 'photo3', 'photo4', 'undercategory']


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = UnderCategory
        fields = ['title']