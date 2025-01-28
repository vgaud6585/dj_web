from django import forms
from .models import User

class UserForm(forms.ModelForm):
   class Meta:
       model = User
       fields = ['usr_heading', 'usr_description', 'usr_code_box', 'usr_image']