from django.db import models
import uuid 

# Create your models here.--> which represents tables.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #null = we dont need to set description FOR DATABASE.
                                                          #blank = keeping value empty still able to save form.
    demo_link = models.CharField(max_length=2000, null=True, blank=True) #eg.= link to live demo
    source_link = models.CharField(max_length=2000, null=True, blank=True)#eg.= github link
    tags = models.ManyToManyField('Tag', blank=True) #many to many relationship with Tag model. used in class Tag below.
    vote_total  = models.IntegerField(default=0, null=True, blank=True) #after review, total upvotes and downvotes.
    vote_ratio = models.IntegerField(default=0, null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True) #automatically set the field to now when the object is first created
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)#using uuid for unique id.

    def __str__(self): #string representation of the model. not django but a python thing
        return self.title #when we print the object it will return title of project.
    
class Review(models.Model): 
    VOTE_TYPE = (
    ('up', 'Up Vote'),
    ('down', 'Down Vote'),
    )
    #owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #IF project is deleted, delete reviews also.
    body = models.TextField(null=True, blank=True)                 #ForeignKey bc one project can have many reviews. 
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True) 
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
        
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True) 
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
