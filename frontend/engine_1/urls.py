from django.urls import path, include

from . import views

app_name = "engine_1"

urlpatterns = [
	path('', views.home, name="home"),
	path('signup/', views.signup, name="signup"),
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('<int:id>/upload', views.user_upload, name="user_upload"),
	path('<int:uid>/upload_index/<int:upload_id>', views.user_upload_index, name="user_upload_index"),
	path('<int:id>/profile', views.user_profile, name="user_profile"),
	path('about/', views.about, name="about"),
	path('', include("django.contrib.auth.urls")),
	path('form/', views.index, name="index"),
    path('viz/', views.viz, name="viz"),
    path('scoreboard/', views.scoreboard, name="scoreboard")
]