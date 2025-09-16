from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),        # 👈 HOME PAGE = LOGIN
    path('login/', views.login_view, name='login'),  # 👈 Mantenha para acessar /login/
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]