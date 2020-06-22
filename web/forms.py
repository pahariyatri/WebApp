from django import forms
from django.contrib import admin
from searcher.models import Destination

class CampgroundQueryAdminForm(forms.ModelForm):
    class Meta:
        model = Destination
        widgets = {
            'categories': forms.widgets.CheckboxSelectMultiple
        }