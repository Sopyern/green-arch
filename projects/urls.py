from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from greenarch import urls


urlpatterns = [
    path("", views.project_list, name="list"),
    re_path(r"^(?P<slug>[\w-]+)/$", views.project_details, name="detail"),
]
