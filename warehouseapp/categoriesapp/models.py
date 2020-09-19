#from django.db import models
from djongo import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class CategoriesApp(models.Model):
    categoryID = models.CharField(max_length=250, unique=True)
    categoryName = models.CharField(max_length=250)
    description = models.TextField()
    picture = models.CharField(max_length=250)

class CategoryForm(ModelForm):
    class Meta:
        model = CategoriesApp
        fields = ['categoryID', 'categoryName', 'description', 'picture']

class UploadCategory(forms.Form):
    categoryID = forms.CharField(max_length=250)
    categoryName = forms.CharField(max_length=250)
    filename = forms.FileField(label=" ", label_suffix="+")

    def sanitizefile(self):
        #print("Self: %s"%(self))
        fle = self.cleaned_data['filename']
        ext = fle.name.split('.')[-1].lower()
        if ext not in ["jpg"]:
            return 0, 0
        return fle, ext
