from django.urls import path
from django.contrib.auth.views import LoginView
import memes.views as views

app_name = 'memes'

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.meme_add, name="add"),
    path('like/', views.meme_like, name="like"),
    path('register/', views.register, name="register"),
    path('waitingroom/', views.waitingroom, name="waitingroom"),
    path('user/<slug:user>/', views.user, name="user"),
    path('logout/', views.logout_view, name="logout"),
    path('status/', views.status, name="status"),
    path('login/', LoginView.as_view(template_name='memes/login.html', redirect_field_name='success'), name="login"),
]


