from rest_framework import permissions


class WriteContributor(permissions.BasePermission):
    """
    Custom permission: only allows users to create a contributor if they are the project author.
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user == view.project.author
        return True

    def has_object_permission(self, request, view, obj):
        return request.user == view.project.author
