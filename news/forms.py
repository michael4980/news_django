from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'url', 'description', 'text', 'is_displayed']
        widgets = {
            'is_displayed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
