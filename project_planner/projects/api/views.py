from projects.models import Project,ProjectAvatar,Task
from .serializers import ProjectSerializer,ProjectCreateSerializer,ProjectUpdateSerializer,TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny

#Retrieve Project
class ProjectRetrieveAPIView(generics.RetrieveAPIView):
    
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    permission_classes=[AllowAny]
  

#Delete Project  (only manager should be able to delete)...
#For now, only admin can
class ProjectDestroyAPIView(generics.DestroyAPIView):
    
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    permission_classes=[IsAdminUser]


#Create Project
class ProjectCreateAPIView(generics.CreateAPIView):
    
    queryset=Project.objects.all()
    serializer_class=ProjectCreateSerializer
    permission_classes=[IsAuthenticated]


#List Projects
class ProjectListAPIView(generics.ListAPIView):
    
    queryset=Project.objects.all().order_by("-start_date")
    serializer_class=ProjectSerializer
    permission_classes=[AllowAny]


#Update Project (only by manager)
class ProjectUpdateAPIView(generics.UpdateAPIView):
    
    queryset=Project.objects.all()
    serializer_class=ProjectUpdateSerializer
    permission_classes=[IsAuthenticated]


#Retrieve Task
class TaskRetrieveAPIView(generics.RetrieveAPIView):
    
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[AllowAny]