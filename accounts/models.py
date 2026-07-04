from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Aggiungiamo campi utili per un e-commerce
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Numero di Telefono")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Indirizzo di Spedizione")

    def __str__(self):
        return f"{self.username} ({self.get_full_name() or self.email})"
