from django.db import models


class Message(models.Model):
    room = models.ForeignKey("Room", related_name='messages', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey("client.User", on_delete=models.CASCADE, null=True)
    audio = models.FileField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        ordering = ('created_at',)


class Room(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=13, unique=True, null=True)

    def __str__(self):
        return self.name