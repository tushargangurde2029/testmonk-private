from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import User_Data


gen=[
    ('Male','Male'),
    ('Female','Female')
]


class Create_User(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class Register_Form(forms.ModelForm):
    gender=forms.CharField(widget=forms.RadioSelect(choices=gen),required=True)
    class Meta:
        model = User_Data
        fields = ['mobile_number','gender','tuser']
    
