from django.shortcuts import render, get_object_or_404
from .models import Job
from .models import Skill

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job ,pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})

def skills(request):
    skills = Skill.objects
    return render(request, 'jobs/skills.html', {'skills':skills})
