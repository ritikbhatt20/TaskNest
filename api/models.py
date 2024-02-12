from django.db import models
from tastypie.resources import ModelResource
from tasks.models import Task

# Create your models here.

class TaskResource(ModelResource):  #it represents the concept of a Movie in a restful api
    class Meta:  # tastypie looks for this inner class Meta
        queryset = Task.objects.all()
        resource_name = 'tasks'
