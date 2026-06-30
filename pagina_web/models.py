from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Lawyer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="lawyer_profile"
    )
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    gps_location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Example: 9.9281, -84.0907"
    )
    webpage = models.URLField(
        blank=True,
        null=True
    )
    carne = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
    )
    photo = models.ImageField(
        upload_to="lawyer_photos/",
        blank=True,
        null=True,

    )

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

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
