from django.db import models

class Service(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix_depart = models.IntegerField()
    image = models.ImageField(upload_to='services/', blank=True)
    details = models.JSONField(default=list, blank=True)
    ordre = models.IntegerField(default=0)
    actif = models.BooleanField(default=True)

    class Meta:
        ordering = ['ordre']
        verbose_name = 'Service'

    def __str__(self):
        return self.nom
