from rest_framework.permissions import IsAuthenticated

class IsTAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return super(IsTAdmin, self).has_permission(request, view) and request.user.user_role == "TAdmin"