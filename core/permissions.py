from re import T
from rest_framework import permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                # admin user has full access to all data
                return True
            elif obj.author == request.user:
                return True
            # elif obj.post and request.user == obj.post.author:
            #     return True # is logged in user is news author
            else:
                return False
        else:
            return False
