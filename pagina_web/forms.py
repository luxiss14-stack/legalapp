from django import forms
from django.contrib.auth.models import User
from .models import Client, Lawyer, Issue, ChatMessage


class ClientRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = [
            "username",
            "password",
            "name",
            "phone",
            "email",
        ]

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"],
        )

        client = Client(
            user=user,
            name=self.cleaned_data["name"],
            phone=self.cleaned_data["phone"],
            email=self.cleaned_data["email"],
        )

        if commit:
            client.save()

        return client


class LawyerRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Lawyer
        fields = [
            "username",
            "password",
            "name",
            "phone",
            "email",
            "gps_location",
            "webpage",
            "carne",
            "photo",
        ]

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"],
        )

        lawyer = Lawyer(
            user=user,
            name=self.cleaned_data["name"],
            phone=self.cleaned_data["phone"],
            email=self.cleaned_data["email"],
            gps_location=self.cleaned_data["gps_location"],
            webpage=self.cleaned_data["webpage"],
            carne=self.cleaned_data["carne"],
            photo=self.cleaned_data.get("photo"),
        )

        if commit:
            lawyer.save()

        return lawyer


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            "title",
            "description",
        ]


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = [
            "message",
        ]

from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        )
    )
