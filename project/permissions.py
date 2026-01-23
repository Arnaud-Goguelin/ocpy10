from rest_framework import permissions


class ContributorReadOnly(permissions.BasePermission):
    """
    Custom permission: only allows users to read Project, Issues, and Comments if they are contributors to the Project.
    """

    def has_permission(self, request, view):
        # import ipdb
        # ipdb.set_trace()
        if request.method not in permissions.SAFE_METHODS:
            return False

        project = getattr(view, "project", None)

        if not project:
            # No project found in view so nothing to check
            return False

        # Check if user is a contributor of the project
        return project.contributors.filter(id=request.user.id).exists() or project.author == request.user

    # do not overwrite has_object_permission because contributors can only read objects they have access to


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
