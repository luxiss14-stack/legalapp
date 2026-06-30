from django import forms
from .models import Client, Lawyer, Issue, ChatMessage


class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "phone", "email"]


class LawyerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ["name", "phone", "email"]


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["title", "description"]


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ["message"]
