from django import forms
import re
from django.core.exceptions import ValidationError




class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='', widget=forms.TextInput(attrs={'autofocus': 'autofocus','size':28, 'maxlength':50,
                        'style': 'font-size: x-large', 'placeholder': 'Enter a pubmed keyword to begin', 'text-align': 'center'}))
    def clean(self):
        unvalidated_data = super(SubmitUrlForm, self).clean()
        url = unvalidated_data.get('url')
        dirt = re.findall(r'[@#$%\^&*\(\)\{\}\[\|\/!~\_\]?<>\.-]', url)

        if dirt == []:
            cleaned_data = unvalidated_data
        else:
            raise ValidationError("Invalid characters in the keyword '%s'" % url)
