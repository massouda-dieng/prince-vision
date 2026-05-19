from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from reservations import views as res_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('portfolio/', core_views.portfolio_view, name='portfolio'),
    path('services/', core_views.services_view, name='services'),
    path('contact/', core_views.contact_view, name='contact'),
    path('reservation/', res_views.reservation_view, name='reservation'),
    path('admin-dashboard/', include('core.dashboard_urls')),
    path('django-admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
