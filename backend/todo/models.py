from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete= models.DO_NOTHING)
    title = models.CharField(max_length=120)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete= models.DO_NOTHING)
    title = models.CharField(max_length=120)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Group(models.Model):
    task = models.ForeignKey(Task, on_delete= models.DO_NOTHING)
    title = models.CharField(max_length=120)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Todo(models.Model):
    group = models.ForeignKey(Group, on_delete= models.DO_NOTHING)
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title