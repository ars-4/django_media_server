from django.urls import path
from guardian import views


urlpatterns = [
    path('register/', views.register, name='RegisterPage'),
    path('login/', views.login_r, name='LoginPage'),
    path('logout/', views.logout_r, name='LogoutPage'),
]