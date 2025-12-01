from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):  #it is just generating form based on model fields in viewspy.
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        } #to show tags as checkbox in form instead of default select multiple widget.

        def __init__(self, *args, **kwargs): #customizing form fields appearance
            super(ProjectForm, self).__init__(*args, **kwargs)
            
            for name, field in self.fields.items(): #iterating through all fields in the form eg:title, description  
                field.widget.attrs.update({'class': 'input input--text'}) 