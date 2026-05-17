from django.contrib import admin
from django.urls import path
from teams import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('player/add/', views.player_create, name='player_create'), # BU SƏTİR ÇATIŞMIR
    path('player/<int:player_id>/', views.player_detail, name='player_detail'),
    path('player/<int:player_id>/edit/', views.player_update, name='player_update'),
    path('player/<int:player_id>/delete/', views.player_delete, name='player_delete'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
]