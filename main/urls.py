from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('advancedratings/<str:className>', views.advancedratings, name="advancedratings"),
    path('schedulepage/<str:userName>', views.schedulepage, name='schedulepage'),
    path('friendLookUp', views.friendLookUp, name='friendLookUp'),
    path('addCourse', views.addCourse, name='addCourse'),
    path('friendUserResults', views.friendUserResults, name='friendUserResults'),

    path('customRedirect', views.customRedirect, name='customRedirect'),

    # Django Auth
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout")

]


# path('accounts/', include('django.contrib.auth.urls')),