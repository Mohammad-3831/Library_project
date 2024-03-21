from django import forms
from Users.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.core import validators


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password :",
                                widget=forms.PasswordInput(attrs={'class': 'form-control rounded text-center'}))
    password2 = forms.CharField(
        label="Confirm Password :", widget=forms.PasswordInput(attrs={'class': 'form-control rounded text-center'})
    )

    class Meta:
        model = User
        fields = ("username",)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control rounded text-center'})
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("username",)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control rounded text-center'}),
                               label="Please Enter Your Username :")
    password = forms.CharField(max_length=150,
                               widget=forms.PasswordInput(attrs={'class': 'form-control rounded text-center'}),
                               label="Please Enter Your Password :")

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if len(email) > 100 :
    #         raise ValidationError('invalid value : %(value)s is invalid',code='invalid',params={'value':f'email'})
    #     return email


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control rounded text-center'}),
                               label="Please Enter Your Username :")
    password1 = forms.CharField(max_length=150,
                                widget=forms.PasswordInput(attrs={'class': 'form-control rounded text-center'}),
                                label="Please Enter Your Password  :")
    password2 = forms.CharField(max_length=150,
                                widget=forms.PasswordInput(attrs={'class': 'form-control rounded text-center'}),
                                label="Please Enter Your Password Again :")

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('invalid value : %(value)s is invalid', code='invalid',
                                  params={'value': f'password1'})
        return password1
