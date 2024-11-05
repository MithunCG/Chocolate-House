# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion
from .forms import SeasonalFlavorForm, IngredientForm, CustomerSuggestionForm

def home(request):
    return render(request, 'home.html')

# SeasonalFlavor CRUD views
def seasonal_flavor_list(request):
    flavors = SeasonalFlavor.objects.all()
    return render(request, 'seasonal_flavor_list.html', {'flavors': flavors})

def seasonal_flavor_create(request):
    if request.method == 'POST':
        form = SeasonalFlavorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seasonal_flavor_list')
    else:
        form = SeasonalFlavorForm()
    return render(request, 'seasonal_flavor_form.html', {'form': form})

def seasonal_flavor_update(request, pk):
    flavor = get_object_or_404(SeasonalFlavor, pk=pk)
    if request.method == 'POST':
        form = SeasonalFlavorForm(request.POST, instance=flavor)
        if form.is_valid():
            form.save()
            return redirect('seasonal_flavor_list')
    else:
        form = SeasonalFlavorForm(instance=flavor)
    return render(request, 'seasonal_flavor_form.html', {'form': form})

def seasonal_flavor_delete(request, pk):
    flavor = get_object_or_404(SeasonalFlavor, pk=pk)
    if request.method == 'POST':
        flavor.delete()
        return redirect('seasonal_flavor_list')
    return render(request, 'seasonal_flavor_confirm_delete.html', {'flavor': flavor})

# Ingredient CRUD views
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredient_list.html', {'ingredients': ingredients})

def ingredient_create(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'ingredient_form.html', {'form': form})

def ingredient_update(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'ingredient_form.html', {'form': form})

def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')
    return render(request, 'ingredient_confirm_delete.html', {'ingredient': ingredient})

def customer_suggestion_view(request):
    if request.method == 'POST':
        form = CustomerSuggestionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the suggestion to the database
            return redirect('customer_suggestion_list')  # Redirect to the customer suggestion list after submission
    else:
        form = CustomerSuggestionForm()  # Create an empty form

    suggestions = CustomerSuggestion.objects.all()  # Get all customer suggestions
    return render(request, 'customer_suggestion_list.html', {'form': form, 'suggestions': suggestions})