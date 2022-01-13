from rest_framework import permissions

class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj.customer is None:
            return True

        return obj.customer == request.user