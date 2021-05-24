from django import forms  
from employee.models import Employee  

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  
		
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1', 'password2', )