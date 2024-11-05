from django import forms
from .models import CustomerSuggestion

class CustomerSuggestionForm(forms.ModelForm):
    class Meta:
        model = CustomerSuggestion
        fields = ['flavor', 'customer_name', 'allergy_concern']
        widgets = {
            'allergy_concern': forms.Textarea(attrs={'rows': 3}),
        }
