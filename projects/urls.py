from django.urls import path
from . import views

urlpatterns =[
    path('', views.projects, name='projects'), #''---> root domain, keep name as it is.
    path('project/<str:pk>/', views.project, name='project'),   #as per 'name' we can access this url in html files.
                                                                #and the changes made in path does not affect the name.
    path('create-project/', views.createProject, name='create-project'),
    path('update-project/<str:pk>/', views.updateProject, name='update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name='delete-project'),
]