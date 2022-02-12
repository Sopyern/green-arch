from django.shortcuts import render
from .models import Members

# Create your views here.


def members(request):
    members = Members.objects.all()
    return render(request, "members/members.html", {"members": members})
