from django.urls import path, include

from . import views

app_name = "engine_1"

urlpatterns = [
	path('', views.home, name="home"),
	path('signup/', views.signup, name="signup"),
	path('login/', views.user_login, name='login'),
	path('<int:id>/upload', views.user_upload, name="user_upload"),
	path('<int:id>/profile', views.user_profile, name="user_profile"),
	path('about/', views.about, name="about"),
	path('', include("django.contrib.auth.urls")),
	path('form/', views.index, name="index"),
    path('viz/', views.viz, name="viz")
]