from django import forms
from .models import Demand
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):    
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data        
        if cd['password'] != cd['password2']:            
            raise forms.ValidationError('Passwords don\'t match.')        
        return cd['password2']


class DemandForm(forms.ModelForm):

    class Meta:
        model = Demand
        fields = ['title', 'phone']