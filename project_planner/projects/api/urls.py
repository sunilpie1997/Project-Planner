from django.urls import path
from .views import ProjectAvatarView,ProjectAvatarUploadView,ProjectCreateAPIView,ProjectDeleteAPIView,ProjectRetrieveAPIView,ProjectListAPIView,ProjectUpdateAPIView,TaskRetrieveAPIView,TaskCreateAPIView,TaskUpdateAPIView,TaskListAPIView,TaskDeleteAPIView


urlpatterns=[
    
    #urls to perform CRUD operations on 'Project' Model
    path('',ProjectListAPIView.as_view(),name='project-list'),
    path('<int:pk>/',ProjectRetrieveAPIView.as_view(),name='project-detail'),
    path('<int:project_id>/delete/',ProjectDeleteAPIView.as_view(),name='project-delete'),
    path('create/',ProjectCreateAPIView.as_view(),name='project-create'),
    path('<int:pk>/update/',ProjectUpdateAPIView.as_view(),name='project-update'),

    #to retrieve image
    path('<int:pk>/image/',ProjectAvatarView.as_view(),name='project-avatar-view'),
    
    #url to upload project avatar (after 'project' has been created)
    path('<int:project_id>/image/<str:filename>/',ProjectAvatarUploadView.as_view(),name='project-avatar-upload'),

    


    #urls to perform CRUD operations on 'Task' Model
    path('<int:project_id>/tasks/',TaskListAPIView.as_view(),name='task-list'),
    path('<int:project_id>/tasks/<int:pk>/',TaskRetrieveAPIView.as_view(),name='task-detail'),
    path('<int:project_id>/tasks/create/',TaskCreateAPIView.as_view(),name='task-create'),
    path('<int:project_id>/tasks/<int:pk>/update/',TaskUpdateAPIView.as_view(),name='task-update'),
    path('<int:project_id>/tasks/<int:task_id>/delete/',TaskDeleteAPIView.as_view(),name='task-delete')
]