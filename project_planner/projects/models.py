from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Project(models.Model):

    manager=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    start_date=models.DateField(null=False,blank=False)
    #validate end_date (should be greater than start_date)
    end_date=models.DateField(null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)

    def __str__(self):
        return str(self.name)


class ProjectAvatar(models.Model):
    project=models.OneToOneField(Project,on_delete=models.CASCADE,primary_key=True,related_name="avatar")
    image=models.FileField()

    def __str__(self):
        return str(self.project)


#'ProjectAvatar' object should be created after 'Project' object creation
@receiver(post_save, sender=Project)
def create_or_update_project_avatar(sender, instance, created, **kwargs):

    if created:
        
        ProjectAvatar.objects.create(project=instance)
    
    instance.avatar.save()
