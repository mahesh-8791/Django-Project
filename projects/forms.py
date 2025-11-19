from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):  #it is just generating form based on model fields in viewspy.
    class Meta:
        model = Project
        fields = '__all__' #all bcz include all attributes in views.py.