from django import forms
from htmx_samples_app.models import Profile

class ProfileModelForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'email'
        ]