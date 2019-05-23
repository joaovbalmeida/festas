from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('event/<int:event_id>/', views.EventsView.as_view(), name='event'),
]