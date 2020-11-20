
    
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #to get json web token on successfull login
    path('auth/login/',TokenObtainPairView.as_view(), name='auth-login'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
