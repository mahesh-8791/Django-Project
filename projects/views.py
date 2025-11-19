from urllib import request
from django.shortcuts import render
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
        context = {'form': form}  #form variable passed to template.
        return render(request, 'projects/project_form.html', context)   