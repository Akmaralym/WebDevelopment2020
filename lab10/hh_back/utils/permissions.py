from rest_framework import permissions


class CompanyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'vacancies':
            return bool(request.user and request.user.is_authenticated)
        return True
