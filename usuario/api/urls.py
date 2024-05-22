from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario-detail'),
]
