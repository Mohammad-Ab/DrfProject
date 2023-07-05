from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsSuperUser(BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.is_superuser )

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        return bool(
                request.method in SAFE_METHODS or
                request.user and
                request.user.is_staff
        )

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(
                request.user.is_authenticated and
                request.user.is_superuser or

                obj.author == request.user
        )

class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self,request,view):
        #if request.method in permissions.SAFE_METHODS and request.user and request.user.is_staff:
            #return True
        return bool(
                request.method in SAFE_METHODS and
                request.user and request.user.is_staff 
                or
                request.user and request.user.is_superuser
        )
