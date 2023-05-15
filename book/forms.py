from django import forms
from .models import BookReview



class BookReviewForm(forms.ModelForm):
    strts_given = forms.IntegerField(min_value=1, max_value=5)
    
    class Meta:
        model = BookReview
        fields  = ('strts_given','comment')

