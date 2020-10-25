from django.db import models


class Message(models.Model):
    user = models.CharField(max_length=25)
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    stars = models.CharField(max_length = 500, default='0|0|0')
    def __str__(self):
        return self.message
    class Meta:
        ordering = ('timestamp',)


class UserName(models.Model):
    user = models.CharField(max_length=25, blank=False, unique=True)
    uid = models.CharField(max_length=100, blank=False, unique=True)
    def __str__(self):
        return self.user
    class Meta:
        ordering = ('user',)
