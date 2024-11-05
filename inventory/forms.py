from django import forms
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion

class SeasonalFlavorForm(forms.ModelForm):
    class Meta:
        model = SeasonalFlavor
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class CustomerSuggestionForm(forms.ModelForm):
    class Meta:
        model = CustomerSuggestion
        fields = '__all__'
