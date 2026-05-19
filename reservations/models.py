from django.db import models
from django.utils import timezone

class Reservation(models.Model):
    TYPE_CHOICES = [
        ('mariage', 'Mariage'),
        ('anniversaire', 'Anniversaire'),
        ('bapteme', 'Baptême'),
        ('shooting', 'Shooting'),
        ('korite', 'Korité'),
        ('tabaski', 'Tabaski'),
        ('evenementiel', 'Événementiel'),
        ('autre', 'Autre'),
    ]
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmé'),
        ('refused', 'Refusé'),
        ('cancelled', 'Annulé'),
    ]
    nom_complet = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    type_evenement = models.CharField(max_length=50, choices=TYPE_CHOICES)
    date_evenement = models.DateField()
    heure_evenement = models.TimeField()
    lieu = models.CharField(max_length=300)
    nombre_personnes = models.IntegerField(null=True, blank=True)
    budget = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    notes_admin = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Réservation'
        verbose_name_plural = 'Réservations'

    def __str__(self):
        return f"{self.nom_complet} - {self.get_type_evenement_display()} - {self.date_evenement}"
