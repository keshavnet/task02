# image upload form

from django import forms
from .models import ImageUpload


class PostForm(forms.ModelForm):

    image = forms.ImageField()
