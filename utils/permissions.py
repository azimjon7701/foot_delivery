from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to admins.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'ADMIN')

class IsWaiter(BasePermission):
    """
    Allows access only to waiters.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'WAITER' or request.user.role == 'ADMIN')

class IsCustomer(BasePermission):
    """
    Allows access only to customers.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'CUSTOMER' or request.user.role == 'ADMIN')