from django.urls import path
from . import views

urlpatterns = [
    path('actores/', views.ActorListView.as_view(), name='actor-list'),
    path('actores/<int:pk>/', views.ActorDetailView.as_view(), name='actor-detail'),
    path('poses/', views.PoseListView.as_view(), name='pose-list'),
    path('poses/<int:pk>/', views.PoseDetailView.as_view(), name='pose-detail'),
    path('ubicaciones/', views.UbicacionListView.as_view(), name='ubicacion-list'),
    path('ubicaciones/<int:pk>/', views.UbicacionDetailView.as_view(), name='ubicacion-detail'),
]