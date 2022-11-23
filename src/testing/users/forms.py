from django import forms
from .models import User
from django.core import validators

class UserForm(forms.Form):
    name = forms.CharField()
    second_name = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify you email:')
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxValueValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('Make sure email match!')

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'













