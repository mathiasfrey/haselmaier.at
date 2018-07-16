from django import forms
from models import Category, Gallery, Picture
# form for uploading a picture file


# form for creating / editing a category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['gallery', 'title', 'slug',]
        widgets = {'gallery': forms.HiddenInput()}

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['category', 'title', 'image']
        widgets = {'category': forms.HiddenInput()}

class DeleteForm(forms.Form):
    pk = forms.IntegerField()