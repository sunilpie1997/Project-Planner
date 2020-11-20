from django.urls import path
from .views import ProjectCreateAPIView,ProjectDestroyAPIView,ProjectRetrieveAPIView,ProjectListAPIView,ProjectUpdateAPIView


urlpatterns=[
    
    #urls to perform CRUD operations on 'Project' Model
    path('',ProjectListAPIView.as_view(),name='project-list'),
    path('<int:pk>/',ProjectRetrieveAPIView.as_view(),name='project-detail'),
    path('<int:pk>/delete/',ProjectDestroyAPIView.as_view(),name='project-destroy'),
    path('create/',ProjectCreateAPIView.as_view(),name='project-create'),
    path('<int:pk>/update/',ProjectUpdateAPIView.as_view(),name='project-update'),
]