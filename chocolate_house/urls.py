from django.urls import path
from django.contrib import admin
from inventory.views import (
    home,
    seasonal_flavor_list,
    seasonal_flavor_create,
    seasonal_flavor_update,
    seasonal_flavor_delete,
    ingredient_list,
    ingredient_create,
    ingredient_update,
    ingredient_delete,
    customer_suggestion_view,
)

urlpatterns = [
  path('', home, name='home'),
    path('seasonal-flavors/', seasonal_flavor_list, name='seasonal_flavor_list'),
    path('seasonal-flavors/create/', seasonal_flavor_create, name='seasonal_flavor_create'),
    path('seasonal-flavors/update/<int:pk>/', seasonal_flavor_update, name='seasonal_flavor_update'),
    path('seasonal-flavors/delete/<int:pk>/', seasonal_flavor_delete, name='seasonal_flavor_delete'),
    path('ingredients/', ingredient_list, name='ingredient_list'),
    path('ingredients/create/', ingredient_create, name='ingredient_create'),
    path('ingredients/update/<int:pk>/', ingredient_update, name='ingredient_update'),
    path('ingredients/delete/<int:pk>/', ingredient_delete, name='ingredient_delete'),
    path('admin', admin.site.urls),
    path('customer-suggestions/', customer_suggestion_view, name='customer_suggestion_list'),
]


