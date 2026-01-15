from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views


app_name = "issue"

issue_router = DefaultRouter()
issue_router.register(r"(?P<project_id>\d+)/issue", views.IssueModelViewSet, basename="issue")

comment_router = DefaultRouter()
comment_router.register(
    r"(?P<project_id>\d+)/issue/(?P<issue_id>\d+)/comment", views.CommentModelViewSet, basename="comment"
)

urlpatterns = [
    path("", include(issue_router.urls)),
    path("", include(comment_router.urls)),
]
