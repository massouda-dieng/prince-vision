from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from reservations.models import Reservation
from portfolio.models import Photo, Category
from contacts.models import Message
from django.utils import timezone
from datetime import timedelta

def dashboard_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('dashboard_home')
        error = 'Identifiants incorrects ou accès non autorisé.'
    return render(request, 'admin_dash/login.html', {'error': error})

def dashboard_logout(request):
    logout(request)
    return redirect('dashboard_login')

@login_required(login_url='/admin-dashboard/login/')
def dashboard_home(request):
    today = timezone.now().date()
    stats = {
        'total_reservations': Reservation.objects.count(),
        'pending': Reservation.objects.filter(statut='pending').count(),
        'confirmed': Reservation.objects.filter(statut='confirmed').count(),
        'this_month': Reservation.objects.filter(created_at__month=today.month).count(),
        'messages_unread': Message.objects.filter(lu=False).count(),
        'photos_count': Photo.objects.count(),
    }
    recent_reservations = Reservation.objects.order_by('-created_at')[:5]
    return render(request, 'admin_dash/dashboard.html', {
        'stats': stats,
        'recent_reservations': recent_reservations,
    })

@login_required(login_url='/admin-dashboard/login/')
def dashboard_reservations(request):
    status_filter = request.GET.get('status', '')
    reservations = Reservation.objects.all()
    if status_filter:
        reservations = reservations.filter(statut=status_filter)
    return render(request, 'admin_dash/reservations.html', {
        'reservations': reservations,
        'status_filter': status_filter,
    })

@login_required(login_url='/admin-dashboard/login/')
@require_POST
def update_reservation_status(request, pk):
    res = get_object_or_404(Reservation, pk=pk)
    new_status = request.POST.get('statut')
    if new_status in ['pending', 'confirmed', 'refused', 'cancelled']:
        res.statut = new_status
        res.save()
        messages.success(request, f'Statut mis à jour: {res.get_statut_display()}')
    return redirect('dashboard_reservations')

@login_required(login_url='/admin-dashboard/login/')
def delete_reservation(request, pk):
    res = get_object_or_404(Reservation, pk=pk)
    res.delete()
    messages.success(request, 'Réservation supprimée.')
    return redirect('dashboard_reservations')

@login_required(login_url='/admin-dashboard/login/')
def dashboard_messages(request):
    msgs = Message.objects.all()
    Message.objects.filter(lu=False).update(lu=True)
    return render(request, 'admin_dash/messages.html', {'messages_list': msgs})

@login_required(login_url='/admin-dashboard/login/')
def dashboard_portfolio(request):
    photos = Photo.objects.select_related('categorie').all()
    categories = Category.objects.all()
    return render(request, 'admin_dash/portfolio.html', {
        'photos': photos,
        'categories': categories,
    })

@login_required(login_url='/admin-dashboard/login/')
@login_required(login_url='/admin-dashboard/login/')
def upload_photo(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        cat_id = request.POST.get('categorie')
        titre = request.POST.get('titre', '')
        if image and cat_id:
            cat = get_object_or_404(Category, pk=cat_id)
            Photo.objects.create(image=image, categorie=cat, titre=titre)
            messages.success(request, 'Photo uploadée avec succès.')
    return redirect('dashboard_portfolio')

@login_required(login_url='/admin-dashboard/login/')
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    messages.success(request, 'Photo supprimée.')
    return redirect('dashboard_portfolio')
