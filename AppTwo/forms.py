from django import forms
from django.core import validators
from AppTwo.models import NewUserReg

# CUSTOM VALIDATOR


def check_name(value):
    if value[0].lower() == 'a':
        raise forms.ValidationError('Yo its works boy')


class MyForm(forms.Form):
    name = forms.CharField(max_length=200, required=True,
                           validators=[check_name])
    email = forms.EmailField(required=True)
    v_email = forms.EmailField(required=True)
    text = forms.CharField(widget=forms.Textarea, validators=[
                           validators.MaxLengthValidator(500)])  # built in validator

    def clean(self):  # this is to clean check whole for
        all_clean_Data = super().clean()
        email = all_clean_Data['email']
        vmail = all_clean_Data['v_email']

        if email != vmail:
            raise forms.ValidationError('EMail doesnot match')


class MyFormSignIn(forms.ModelForm):
    
    class Meta:
        model = NewUserReg
        fields = '__all__'
