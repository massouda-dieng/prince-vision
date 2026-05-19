from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Reservation
from .forms import ReservationForm

def reservation_view(request):
    form = ReservationForm()
    success = False
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            res = form.save()
            success = True
            # Email confirmation
            try:
                send_mail(
                    f'Confirmation de réservation - TEOPICTURE',
                    f'Bonjour {res.nom_complet},\n\nVotre réservation pour {res.get_type_evenement_display()} le {res.date_evenement} à {res.heure_evenement} a bien été reçue.\n\nNous vous contacterons rapidement pour confirmer.\n\nTEOPICTURE\n+221 77 344 67 60',
                    settings.DEFAULT_FROM_EMAIL,
                    [res.email],
                    fail_silently=True,
                )
            except:
                pass
            form = ReservationForm()
    return render(request, 'reservation/reservation.html', {'form': form, 'success': success})
