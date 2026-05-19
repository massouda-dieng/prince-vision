from django.shortcuts import render
from portfolio.models import Photo, Category
from contacts.models import Testimonial
from services_app.models import Service

def home(request):
    photos_featured = Photo.objects.filter(featured=True)[:8]
    testimonials = Testimonial.objects.filter(actif=True)[:6]
    services = Service.objects.filter(actif=True)[:6]
    return render(request, 'home/home.html', {
        'photos_featured': photos_featured,
        'testimonials': testimonials,
        'services': services,
    })

def portfolio_view(request):
    categories = Category.objects.all()
    cat_slug = request.GET.get('cat', '')
    if cat_slug:
        photos = Photo.objects.filter(categorie__slug=cat_slug)
    else:
        photos = Photo.objects.all()
    return render(request, 'portfolio/portfolio.html', {
        'categories': categories,
        'photos': photos,
        'cat_active': cat_slug,
    })

def services_view(request):
    services = Service.objects.filter(actif=True)
    return render(request, 'services/services.html', {'services': services})

def contact_view(request):
    success = False
    if request.method == 'POST':
        from contacts.models import Message
        Message.objects.create(
            nom=request.POST.get('nom', ''),
            email=request.POST.get('email', ''),
            telephone=request.POST.get('telephone', ''),
            sujet=request.POST.get('sujet', ''),
            message=request.POST.get('message', ''),
        )
        success = True
    return render(request, 'contact/contact.html', {'success': success})
