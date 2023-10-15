from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label='name',max_length=50)
    email=forms.EmailField(label='email',max_length=50)
    message=forms.CharField(label='MESSEGE',max_length=300)