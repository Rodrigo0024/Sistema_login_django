from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)
    email = models.EmailField(unique=True)  # 👈 Este campo deve existir!

    def __str__(self):
        return self.username