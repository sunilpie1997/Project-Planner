from django.db import models
from django.conf import settings
from projects.models import Project


class Task(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    start_date=models.DateField(null=False,blank=False)
    end_date=models.DateField(null=False,blank=False)
    #'status' indicates task completion status. 'True' indicates completed
    status=models.BooleanField(default=False,blank=True)
    assignee=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET_NULL,related_name="tasks_assigned")
    description=models.TextField(max_length=500,null=False,blank=False)

    def __str__(self):
        return str(self.project)+" -> "+str(self.name)+" for "+str(self.assignee)
