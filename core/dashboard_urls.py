from django.urls import path
from . import dashboard_views

urlpatterns = [
    path('', dashboard_views.dashboard_home, name='dashboard_home'),
    path('login/', dashboard_views.dashboard_login, name='dashboard_login'),
    path('logout/', dashboard_views.dashboard_logout, name='dashboard_logout'),
    path('reservations/', dashboard_views.dashboard_reservations, name='dashboard_reservations'),
    path('reservations/<int:pk>/statut/', dashboard_views.update_reservation_status, name='update_reservation_status'),
    path('reservations/<int:pk>/delete/', dashboard_views.delete_reservation, name='delete_reservation'),
    path('messages/', dashboard_views.dashboard_messages, name='dashboard_messages'),
    path('portfolio/', dashboard_views.dashboard_portfolio, name='dashboard_portfolio'),
    path('portfolio/upload/', dashboard_views.upload_photo, name='upload_photo'),
    path('portfolio/<int:pk>/delete/', dashboard_views.delete_photo, name='delete_photo'),
]
