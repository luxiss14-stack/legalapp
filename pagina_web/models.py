from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Lawyer(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="issues"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name} - {self.title}"


class ChatMessage(models.Model):
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    lawyer = models.ForeignKey(
        Lawyer,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    message = models.TextField()
    sent_by_lawyer = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        sender = "Lawyer" if self.sent_by_lawyer else "Client"
        return f"{sender}: {self.message[:40]}"
