from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse

from projects.forms import ProjectForm
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    
    return render(request, 'projects/single-project.html', {'project': projectObj})

def createProject(request): 
        form = ProjectForm()

        if request.method == 'POST':        #CRUD Operation --> Create, Read, Update, Delete
            form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects') #user redirected to projects page after creating project.

        context = {'form': form}  #form variable passed to template.
        return render(request, 'projects/project_form.html', context) 


def updateProject(request, pk): 
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project) # instance is project that we want to update.

    if request.method == 'POST':        #CRUD Operation --> Create, Read, Update, Delete
        form = ProjectForm(request.POST, instance=project) # #to check which project to update.
    if form.is_valid():
        form.save()
        return redirect('projects') #user redirected to projects page after creating project.

    context = {'form': form}  #form variable passed to template.
    return render(request, 'projects/project_form.html', context) 


def deleteProject(request, pk):
     project = Project.objects.get(id=pk) #to pass the object to template.
     if request.method == 'POST':
         project.delete()
         return redirect('projects') #after deletion redirect to projects page.
     context = {'object': project}
     return render(request, 'projects/delete_template.html', context)