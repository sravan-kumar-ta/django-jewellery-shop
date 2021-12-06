from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from account.forms import LoginForm


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('login/',
         auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm), name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name="logout"),
]
