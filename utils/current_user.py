import contextvars

from django.core.handlers.wsgi import WSGIRequest
from django.utils.deprecation import MiddlewareMixin

user_id = contextvars.ContextVar('user_id', default='0')


def get_current_user_id():
    return user_id.get()


def _set_current_user_id(id):
    user_id.set(str(id))


class GlobalUserMiddleware(MiddlewareMixin):
    def process_request(self, request: WSGIRequest):
        id = 0
        if hasattr(request, 'user') and request.user.is_authenticated:
            id = getattr(request.user, 'id')
        _set_current_user_id(id)


