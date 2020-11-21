
    
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView


urlpatterns = [

    path('',HomePageView.as_view(),name="homepage"),

    #this view is for changing passwords,viewing details,profile directly on this server
    path('accounts/',include("accounts.urls")),

    #to retrieve user details through api
    path('user/',include('accounts.api.urls')),

    #this is for oauth 2.0 using google
    path('oauth/', include('social_django.urls', namespace='social')),


    path('admin/', admin.site.urls),

    #to get json web token on successfull login
    path('auth/login/',TokenObtainPairView.as_view(), name='auth-login'),

    #api for projects
    path('api/projects/',include('projects.api.urls'),name='projects-api' ),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
