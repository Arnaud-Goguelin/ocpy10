from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views


# ** PROJECT MANAGEMENT **
#     - enpoints:
#            api/projects/ # for admin users
#            api/project/ (post)
#            api/project/<id:pk>/ (get, update, delete)
#            api/project/<id:pk>/contributors/ (get, post)
#            api/project/<project_id:pk>/contributors/<id:pk>/ (delete)
#
#     get project
#     create project
#     delete project
#     update project
#     assigned contributors to project

app_name = "project"
project_router = DefaultRouter()
project_router.register(r"", views.ProjectModelViewSet, basename="project")

contributor_router = DefaultRouter()
contributor_router.register(r"(?P<project_id>\d+)/contributors", views.ContributorModelViewSet, basename="contributor")

urlpatterns = [
    path("", include(project_router.urls)),
    path("", include(contributor_router.urls)),
]
