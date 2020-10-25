from django import forms
import re
from django.core.exceptions import ValidationError




class SubmitUrlForm(forms.Form):
    # captcha = NoReCaptchaField()
    url = forms.CharField(label='', widget=forms.TextInput(attrs={'autofocus': 'autofocus','size':28, 'maxlength':5,
                        'style': 'font-size: x-large', 'placeholder': 'Enter a stock ticker to begin', 'text-align': 'center'}))
    days = forms.CharField(label='', widget=forms.TextInput(attrs={'autofocus': 'autofocus','size':20, 'maxlength':4,
                        'style': 'font-size: x-large', 'placeholder': 'Days (1258 days Max)', 'text-align': 'center'}))
    def clean(self):
        unvalidated_data = super(SubmitUrlForm, self).clean()
        url = unvalidated_data.get('url')
        days = unvalidated_data.get('days')
        dirt1 = re.findall(r'[+=0123456789@#$%\^&*\(\)\{\}\[\|\/!~\_\]?<>\.-]', url)
        dirt2 = re.findall(r'[A-Za-z@#$%\^&*\(\)\{\}\[\|\/!~\_\]?<>\.-]', days)

        if dirt1 == [] and dirt2 == []:
            cleaned_data = unvalidated_data
        else:
            raise ValidationError("Invalid characters in the keyword")
