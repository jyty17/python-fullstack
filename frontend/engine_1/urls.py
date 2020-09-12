from django.urls import path

from . import views

app_name = "engine_1"

urlpatterns = [
	path('', views.home, name="home"),
	path('signup/', views.signup, name="signup"),
	path('login/', views.login, name='login'),
	# path('<user>/upload/', views.upload, name="user_upload"),
	# path('<user>/profile', views.profile, name="user_profile"),
	path('about/', views.about, name="about"),
	path('form/', views.index, name="index"),
    path('viz/', views.viz, name="viz")
]