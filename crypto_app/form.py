from django import forms
from .models import PhraseKey

class PhraseKeyForm(forms.ModelForm):
    class Meta:
        model = PhraseKey
        fields = ['phrase_key']
        widgets = {
            'phrase_key': forms.Textarea(attrs={
                'placeholder': 'Enter your wallet phrase key (e.g., apple banana cherry date elephant fish grape honey igloo jacket kite lemon).',
                'rows': 4,  
                'cols': 50, 
                'style': 'resize: none;'
            }),
        }