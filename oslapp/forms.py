from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from oslapp.models import Document, Profile


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    bio = forms.CharField(widget=forms.Textarea, help_text='Your bio')
    is_private = forms.BooleanField(help_text='Check it if you want your account private')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'birth_date')


class FooForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'birth_date')
