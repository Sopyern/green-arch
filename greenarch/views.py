from django.shortcuts import render
from projects.models import Project
from django.core.mail import send_mail


def homepage(request):
    return render(request, "homepage.html")


def team_members(request):
    return render(request, "members.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("contactName")
        email = request.POST.get("contactEmail")
        subject = request.POST.get("contactSubject")
        message = request.POST.get("contactMessage")

        message_note = """
        from:{}
        New message: {}
        """.format(
            email, message
        )
        send_mail(
            name,
            message_note,
            email,
            ["greenarchassociatesngn@gmail.com"],
        )
        return render(request, "contact.html", {"name": name})
    else:
        return render(request, "contact.html", {})
