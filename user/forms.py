from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import RadioSelect


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() 
    phone_no = forms.CharField(max_length = 20) 
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    account_type = forms.ChoiceField(choices=(('Employee','Employee'), ('Employer','Employer')), widget=RadioSelect())
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1','password2']