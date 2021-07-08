from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)

    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name}'
