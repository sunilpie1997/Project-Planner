from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

#custom user model
User = get_user_model()


#Retrieve user 
class UserRetrieveAPIView(RetrieveAPIView):
    
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]
    
    def get_object(self):
    
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset,id=self.request.user.id)
    
        return obj
  
