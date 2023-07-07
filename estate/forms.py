from django import forms

from estate.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'id':'input-1', 'autocomplete':'off', 'name':'form[]', 'placeholder':'here...', 'class':'form-subscribe__input'})
        }