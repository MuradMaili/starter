
from django import forms
from . models import Contact
from django.contrib.auth.forms import UserCreationForm
class ContactFrom(forms.ModelForm):

    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'First Name:'
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Last Name:'
    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Email:'
    }))
    phone=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Phone number:'
    }))
    message=forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Your message'
    }))

    class Meta:
        model=Contact
        fields=['first_name','last_name','email','phone','message']
    


