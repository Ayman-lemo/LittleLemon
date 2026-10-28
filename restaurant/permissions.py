from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, _view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name='Manager').exists()
        )


class IsManagerOrDeliveryCrew(BasePermission):
    def has_permission(self, request, _view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(
                name__in=['Manager', 'Delivery crew']
            ).exists()
        )