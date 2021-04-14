from django.forms import ModelForm 
from django import forms
from .models import Review

class ReviewForm(ModelForm):
    class Meta: 
        model = Review
        widgets = {
          'review': forms.Textarea(attrs={'rows':3, 'cols':20}),
        }
        fields = ['review', 'rating']