
from django import forms

class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for i, clabel in enumerate(extra):
            self.fields['custom_%s' % i] = forms.CharField(label=clabel)

    def extra_data(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('custom_'):
                yield (self.fields[name].label, value)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
           raise forms.ValidationError("The two password fields didn't match.")
        return password2
