from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):  #it is just generating form based on model fields in viewspy.
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image',
                   'demo_link', 'demo_link', 'source_link', 'tags']