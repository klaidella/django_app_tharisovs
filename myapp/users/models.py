from django.db import models
from django.urls import reverse

class Users(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:get_user', kwargs={'pk': self.id})
