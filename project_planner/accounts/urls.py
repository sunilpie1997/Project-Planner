from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView
from .views import ProfileView,ChangePasswordView

"""
these views are django auth views.
You need not create your own views.

there is no view for registring user except through 'google' account on Login page
"""

urlpatterns = [

path('profile/',ProfileView.as_view(),name="profile"),
path('login/',LoginView.as_view(template_name="login.html"),name="login"),
path('logout/',LogoutView.as_view(template_name="logout.html"),name="logout"),
path('change_password/',ChangePasswordView.as_view(template_name="password_change.html"),name='password_change'),
path('password_change/done/',PasswordChangeDoneView.as_view(template_name="password_change_done.html"),name='password_change_done')

]