from django.forms import ModelForm 
from django import forms
from .models import Review

class ReviewForm(ModelForm):
    class Meta: 
        model = Review
        widgets = {
          'review': forms.Textarea(attrs={
            'rows':3, 
            'cols':20,
            'placeholder': 'Add comment...',
            'style': 'width: 15em;'
            }),
        }
        label=False
        fields = ['review', 'rating']