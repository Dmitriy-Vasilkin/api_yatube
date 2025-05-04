from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsAuthor(IsAuthenticated):
    """Разрешение запросов для аутентифицированных пользователей."""

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS or obj.author == request.user)
