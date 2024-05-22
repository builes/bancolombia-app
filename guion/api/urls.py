from django.urls import path
from . import views

urlpatterns = [
    path('dialogos/', views.DialogoListView.as_view(), name='dialogo-list'),
    path('dialogos/<int:pk>/', views.DialogoDetailView.as_view(), name='dialogo-detail'),
    path('escenas/', views.EscenaListView.as_view(), name='escena-list'),
    path('escenas/<int:pk>/', views.EscenaDetailView.as_view(), name='escena-detail'),
    path('guiones/', views.GuionList.as_view(), name='guion-list'),
    path('guiones/<int:pk>/', views.GuionDetail.as_view(), name='guion-detail'),
    path('historial_cambios/', views.HistorialCambiosList.as_view(), name='historial-cambios-list'),
    path('historial_cambios/<int:pk>/', views.HistorialCambiosDetail.as_view(), name='historial-cambios-detail'),
]
