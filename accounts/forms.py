from django import forms
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=25,required=True)
    password=forms.CharField(widget=forms.PasswordInput)
