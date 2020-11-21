from rest_framework import serializers
from django.contrib.auth import get_user_model

#custom user model  
User = get_user_model()


# user serializer (for retrieval)
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
    
        model=User
        fields=['username','email','first_name','last_name','is_staff','last_login']