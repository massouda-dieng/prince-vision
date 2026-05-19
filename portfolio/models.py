from django.db import models

class Category(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordre']
        verbose_name = 'Catégorie'

    def __str__(self):
        return self.nom

class Photo(models.Model):
    titre = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='portfolio/')
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='photos')
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    ordre = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordre', '-created_at']
        verbose_name = 'Photo'

    def __str__(self):
        return f"{self.categorie.nom} - {self.titre or self.id}"
