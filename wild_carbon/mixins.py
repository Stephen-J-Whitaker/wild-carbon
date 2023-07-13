from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Class to test if a logged in user is a superuser before they can
    use a view.
    Code sourced at:
    https://stackoverflow.com/questions/67351312/ ...
    django-check-if-superuser-in-class-based-view
    """
    def test_func(self):
        return self.request.user.is_superuser
