from projects.models import Project,ProjectAvatar,Task
from .serializers import ProjectSerializer,ProjectCreateSerializer,ProjectUpdateSerializer,TaskSerializer,TaskUpdateSerializer,TaskCreateSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#Retrieve Project
class ProjectRetrieveAPIView(generics.RetrieveAPIView):
    
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    permission_classes=[AllowAny]
  

#Delete Project  (only manager should be able to delete)...
class ProjectDeleteAPIView(APIView):
    
    #Before changing below permission to 'AllowAny', add additional check in below 'delete()' code
    permission_classes=[IsAuthenticated]

    def delete(self,request,project_id,format=None):

        project_id=self.kwargs['project_id']
        
        if isinstance(project_id,int):

            project_exists=Project.objects.filter(pk=project_id).exists()
            
            if project_exists:
                project=Project.objects.get(pk=project_id)
                
                if request.user==project.manager:
                    project.delete()
                    return Response(status=status.HTTP_200_OK)

                else:
                    return Response({"detail":"You don't have permission to delete"},status=status.HTTP_401_UNAUTHORIZED)

            else:
                return Response({"detail":"project with given id does not exist"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail":"enter valid project id"},status=status.HTTP_400_BAD_REQUEST)


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


#task create view
class TaskCreateAPIView(generics.CreateAPIView):

    queryset=Task.objects.all()
    serializer_class=TaskCreateSerializer
    permission_classes=[AllowAny]

    def get_serializer_context(self):
    
        context=super().get_serializer_context()
        context.update({"project_id":self.kwargs['project_id']})
    
        return context


#to update task
class TaskUpdateAPIView(generics.UpdateAPIView):

    queryset=Task.objects.all()
    serializer_class=TaskUpdateSerializer
    permission_classes=[AllowAny]

    def get_serializer_context(self):
    
        context=super().get_serializer_context()
        context.update({"project_id":self.kwargs['project_id']})
    
        return context


#List tasks in each project
class TaskListAPIView(generics.ListAPIView):

    serializer_class=TaskSerializer
    permission_classes=[AllowAny]

    #only tasks with given project_id
    def get_queryset(self):

        project_id = self.kwargs['project_id']
        return Task.objects.filter(project_id=project_id)


#to delete task for a particular project
class TaskDeleteAPIView(APIView):

    #Before changing this permission to 'AllowAny', place additional check in below 'delete()' code
    permission_classes=[IsAuthenticated]

    def delete(self,request,project_id,task_id,format=None):

        project_id=self.kwargs['project_id']
        
        if isinstance(project_id,int) and isinstance(task_id,int):

            project_exists=Project.objects.filter(pk=project_id).exists()
            task_id=Task.objects.filter(pk=task_id).exists()
            
            if project_exists and task_id:
                project=Project.objects.get(pk=project_id)
                task=Task.objects.get(pk=task_id)

                if task.project==project:
                
                    if request.user==project.manager:
                        task.delete()
                        return Response(status=status.HTTP_200_OK)

                    else:
                        return Response({"detail":"You don't have permission to delete"},status=status.HTTP_401_UNAUTHORIZED)

                else:
                    return Response({"detail":"given task does not exist in given project"},status=status.HTTP_200_OK)

            else:
                return Response({"detail":"project with given id or task with given id does not exist"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail":"enter valid project id and task_id"},status=status.HTTP_400_BAD_REQUEST)