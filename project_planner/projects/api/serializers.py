from rest_framework import serializers
from projects.models import Project,ProjectAvatar,Task
from django.contrib.auth import get_user_model

User=get_user_model()


#to view 'manager' in project
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["username","first_name","last_name"]


#to view project details
class ProjectSerializer(serializers.ModelSerializer):
    
    manager=UserSerializer()
    class Meta:
        model=Project
        fields=['name',"manager",'start_date','end_date','description']


#to create new Project
class ProjectCreateSerializer(serializers.ModelSerializer):
    name=serializers.CharField(required=True,max_length=50,min_length=3)
    start_date=serializers.DateField(required=True)
    end_date=serializers.DateField(allow_null=True)
    description=serializers.CharField(required=True,max_length=500,min_length=3)

    class Meta:
        model=Project
        fields=['name','start_date','end_date','description']
    
    def create(self,validated_data):

        request = self.context.get('request', None)

        if request.auth is not None:

            user=request.user
            name=validated_data.get("name")
            start_date=validated_data.get("start_date")
            end_date=validated_data.get("end_date")
            description=validated_data.get("description")

            new_project=Project.objects.create(manager=user,name=name,start_date=start_date,end_date=end_date,description=description)
            return new_project
        else:

            raise serializers.ValidationError("authentication credentials were not provided")

#to update project
class ProjectUpdateSerializer(serializers.ModelSerializer):

    name=serializers.CharField(required=True,max_length=50,min_length=3)
    start_date=serializers.DateField(required=True)
    end_date=serializers.DateField(allow_null=True)
    description=serializers.CharField(required=True,max_length=500,min_length=3)

    class Meta:
        model=Project
        fields=['name','start_date','end_date','description']
    
    def update(self,instance,validated_data):

        request = self.context.get('request', None)

        if request.auth is not None:

            user=request.user

            if instance.manager==user:

                instance.name=validated_data.get("name")
                instance.start_date=validated_data.get("start_date")
                instance.end_date=validated_data.get("end_date")
                instance.description=validated_data.get("description")

                instance.save(force_update=True)
                return instance
            
            else:
                raise serializers.ValidationError("you don't have required permission")
        else:
            raise serializers.ValidationError("authentication credentials were not provided")


#to view Task
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model=Task
        fields=["name","start_date","end_date","description"]
