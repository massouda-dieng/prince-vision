from django.db import models
from django.utils import timezone

class Message(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)
    sujet = models.CharField(max_length=300)
    message = models.TextField()
    lu = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Message'

    def __str__(self):
        return f"{self.nom} - {self.sujet}"

class Testimonial(models.Model):
    nom = models.CharField(max_length=200)
    texte = models.TextField()
    note = models.IntegerField(default=5)
    type_service = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Témoignage'

    def __str__(self):
        return f"{self.nom} - {self.note}★"
