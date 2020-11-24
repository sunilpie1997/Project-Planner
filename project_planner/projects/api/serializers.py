from rest_framework import serializers
from projects.models import Project,ProjectAvatar,Task
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User=get_user_model()


#to view 'manager' in project
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]


#to show project avatar
class ProjectAvatarSerializer(serializers.ModelSerializer):

    class Meta:

        model=ProjectAvatar
        fields=['image']


#to view project details
class ProjectSerializer(serializers.ModelSerializer):
    
    manager=UserSerializer()
    class Meta:
        model=Project
        fields=['id','name',"manager",'start_date','end_date','description']


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

    assignee=UserSerializer()
    class Meta:
        model=Task
        fields=["id","name","start_date","end_date","description","status","assignee"]


#to create task
class TaskCreateSerializer(serializers.ModelSerializer):

    name=serializers.CharField(required=True,max_length=50,min_length=3)
    start_date=serializers.DateField(required=True)
    end_date=serializers.DateField(required=True)
    description=serializers.CharField(required=True,max_length=100,min_length=3)
    status=serializers.BooleanField(default=False,required=False)
    username=serializers.CharField(min_length=3,max_length=100,allow_null=True)

    class Meta:
        model=Task
        fields=["name","start_date","end_date","description","status","username"]

    def create(self,validated_data):

        #get request
        request = self.context.get('request', None)

        #if request is authenticated?
        if request.auth is not None:

            #get project_id from context
            project_id=self.context.get("project_id")

            #if project exists?
            project_exist=Project.objects.filter(pk=project_id).exists()

            if project_exist:
                
                project=Project.objects.get(pk=project_id)

                #if project's manager is same as user in request?
                if project.manager==request.user:

                    name=validated_data.get("name")
                    start_date=validated_data.get("start_date")
                    end_date=validated_data.get("end_date")
                    description=validated_data.get("description")
                    status=validated_data.get("status")
                    username=validated_data.get("username")

                    if username is not None:

                        #if assignee exist?
                        assignee_exist=User.objects.filter(username=username).exists()

                        if assignee_exist:
                            assignee=User.objects.get(username=username)
                            new_task=Task.objects.create(project=project,name=name,start_date=start_date,end_date=end_date,description=description,status=status,assignee=assignee)
                            return new_task
                        else:

                            raise serializers.ValidationError("assignee with given username doesn't exist")
                    
                    else:
                        new_task=Task.objects.create(project=project,name=name,start_date=start_date,end_date=end_date,description=description,status=status)
                        return new_task
                
                else:
                    raise serializers.ValidationError("you don't have required permission to create task in this project")
            
            else:
                raise serializers.ValidationError("project with given id does not exist")
        
        else:
            raise serializers.ValidationError("authentication credentials were not provided")



#to update task
class TaskUpdateSerializer(serializers.ModelSerializer):

    name=serializers.CharField(required=True,max_length=50,min_length=3)
    start_date=serializers.DateField(required=True)
    end_date=serializers.DateField(required=True)
    description=serializers.CharField(required=True,max_length=100,min_length=3)
    status=serializers.BooleanField(default=False,required=False)
    username=serializers.CharField(min_length=3,max_length=100,allow_null=True)

    class Meta:
        model=Task
        fields=["name","start_date","end_date","description","status","username"]

    def update(self,instance,validated_data):

        #get request
        request = self.context.get('request', None)

        #if request is authenticated?
        if request.auth is not None:

            #get project_id from context
            project_id=self.context.get("project_id")

            #if project exists?
            project_exist=Project.objects.filter(pk=project_id).exists()

            if project_exist:
                
                project=Project.objects.get(pk=project_id)

                #if project's manager is same as user in request?
                if project.manager==request.user:

                    instance.name=validated_data.get("name")
                    instance.start_date=validated_data.get("start_date")
                    instance.end_date=validated_data.get("end_date")
                    instance.description=validated_data.get("description")
                    instance.status=validated_data.get("status")
                    username=validated_data.get("username")

                    if username is not None:
                        #if assignee exist?
                        assignee_exist=User.objects.filter(username=username).exists()

                        if assignee_exist:
                            instance.assignee=User.objects.get(username=username)
                            instance.save(force_update=True)
                            return instance
                        else:
                            raise serializers.ValidationError("assignee with given username doesn't exist")
                    
                    else:
                        instance.assignee=None
                        instance.save(force_update=True)
                        return instance

                else:
                    raise serializers.ValidationError("you don't have required permission to create task in this project")
            
            else:
                raise serializers.ValidationError("project with given id does not exist")
        
        else:
            raise serializers.ValidationError("authentication credentials were not provided")