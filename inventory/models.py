from django.db import models
from django.utils import timezone
import datetime


class SeasonalFlavor(models.Model):
    MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]

    SEASON_CHOICES = [
        ('Winter', 'Winter'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall', 'Fall'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Optional field for flavor description
    available_month = models.CharField(max_length=20, choices=MONTH_CHOICES, default='January')
    season = models.CharField(max_length=20, choices=SEASON_CHOICES, default='Winter')  # New field for season

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()  # Quantity in grams or any other unit
    unit = models.CharField(max_length=50)  # E.g., grams, liters, etc.

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"


class CustomerSuggestion(models.Model):
    flavor = models.CharField(max_length=100, null=True)
    customer_name = models.CharField(max_length=100)
    allergy_concern = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"Feedback from {self.customer_name} on {self.flavor}"
