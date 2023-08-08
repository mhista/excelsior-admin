
from django.contrib.auth.mixins import AccessMixin, PermissionRequiredMixin
from django.shortcuts import redirect, reverse

class CreateUpdateStudent(AccessMixin):
    pass
    # """Verify that the current user is authenticated."""
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect(reverse('student:index'))
    #     return super().dispatch(request, *args, **kwargs)


# class UserHasInfo(AccessMixin):
#     """Verify that the current user is authenticated."""
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.has_userinfo_accounts:
#             return redirect(reverse('ecoverse:account-info-update', kwargs= {'pk': kwargs['pk']}))
#         return super().dispatch(request, *args, **kwargs)

