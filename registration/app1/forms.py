from django import forms
from .models import UserProfile

class BalanceUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['balance']
