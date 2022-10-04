"""authProject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('usercrear/', views.CrearUsuarioView.as_view()),
    path('user/<int:pk>', views.UsuarioView.as_view()),
    path('personalsaludCrear/', views.CrearPersonalSaludView.as_view()),
    path('personalsalud/<int:pk>', views.PersonalSaludView.as_view()),
    path('familiarcrear/', views.CrearFamiliaresView.as_view()),
    path('familiar/<int:pk>',views.FamiliaresView.as_view()),
    path('historiacrear/', views.CrearHistoriaClinicaView.as_view()),
    path('historia/<int:pk>',views.HistoriaClinicaView.as_view()),
    path('pacientecrear/', views.CrearPacientesView.as_view()),
    path('paciente/<int:pk>',views.PacientesView.as_view()),
    path('signoscrear/', views.CrearSignosVitalesView.as_view()),
    path('signos/<int:pk>',views.SignosVitalesView.as_view()),

]
