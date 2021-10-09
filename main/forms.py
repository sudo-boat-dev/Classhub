from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import UserProfile

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('role','branch','academic_year')




