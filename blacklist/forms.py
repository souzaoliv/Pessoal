from .models import Blacklist
from django import forms

class BlacklistForm(forms.ModelForm):
    class Meta:
        model = Blacklist
        fields = ['ip_address']
        widgets = {
            'ip_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o endereço IP'}),
        }
