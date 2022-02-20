from django import forms
from .models import *


class Menu_ItemForm(forms.ModelForm):
    class Meta:
        model=Menu_Item
        exclude=[]


class MenuForm(forms.ModelForm):
    class Meta:
        model=Menu
        exclude=[]


class TableForm(forms.ModelForm):
    class Meta:
        model=Table
        exclude=[]


class Order_ItemForm(forms.ModelForm):
    class Meta:
        model=Order_Item
        exclude=[]


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        exclude=[]




