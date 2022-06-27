from django.http import Http404


class UserRightsMixin:
    def has_permission(self):
        if self.request.user.is_superuser or self.request.user.is_moderator:
            return True

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)
