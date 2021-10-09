from django.forms import fields
from .models import Fruits
from django import forms

class FruitsForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields = '__all__'
        labels = {
            'no':'No.',
            'name':'果物名',
            'memo':'メモ',
            }