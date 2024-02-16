from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home.html'),
    path('advancedratings', views.advancedratings, name="advancedratings.html"),
    path('schedulepage', views.schedulepage, name='schedulepage.html'),
#    path('login', views.login, name="login.html"),

    # Django Auth
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login')
]


# path('accounts/', include('django.contrib.auth.urls')),