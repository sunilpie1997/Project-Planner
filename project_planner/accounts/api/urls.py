from django.urls import path
from .views import UserRetrieveAPIView


urlpatterns=[

   #to retrieve user details (GET)
    path('',UserRetrieveAPIView.as_view(),name='user-detail'),
  
]
    