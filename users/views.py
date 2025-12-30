from django.shortcuts import render
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk) # Get profile by primary key

    topSkills = profile.skill_set.exclude(description__exact="") #profile--child obj, skill--child model
    #if skill dont have description then exclude it from topSkills
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills} # Pass profile to context
    return render(request, 'users/user-profile.html', context)
