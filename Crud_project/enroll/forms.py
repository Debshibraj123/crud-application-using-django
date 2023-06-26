from django import forms
from .models import User, School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name','address','contact']

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'school']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput( render_value=True, attrs={'class':'form-control'}),
            
        }
        
