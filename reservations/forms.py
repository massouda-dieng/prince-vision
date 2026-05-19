from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom_complet', 'telephone', 'email', 'type_evenement', 'date_evenement', 'heure_evenement', 'lieu', 'nombre_personnes', 'budget', 'message']
        widgets = {
            'nom_complet': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Votre nom complet'}),
            'telephone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+221 XX XXX XX XX'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'votre@email.com'}),
            'type_evenement': forms.Select(attrs={'class': 'form-input'}),
            'date_evenement': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'heure_evenement': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'lieu': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Lieu de l\'événement'}),
            'nombre_personnes': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Nombre de personnes'}),
            'budget': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Budget estimé (FCFA)'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Informations complémentaires...'}),
        }
