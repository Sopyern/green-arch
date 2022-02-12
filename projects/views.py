import projects
from django.shortcuts import render
from django.http import HttpResponse

from .models import Project


def project_details(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, "projects/project_detail.html", {"project": project})


def project_list(request):
    projects = Project.objects.all().order_by("date")
    return render(request, "projects/project_lidy.html", {"projects": projects})
