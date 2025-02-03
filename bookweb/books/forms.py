from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import ClassicUser
from django import forms



class OrderForm(ModelForm):
    class Meta:
        model = ClassicUser
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)  # Get the user instance without saving yet
        user.email = self.cleaned_data['email']  # You can customize the email field here
        if commit:
            user.save()  # Save the user instance to the database
        return user
