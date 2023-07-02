from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Class to test if a logged in user is a superuser before they can
    use a view.
    Code sourced at: plants/templates/plants/list_plant_records.html
    """
    def test_func(self):
        return self.request.user.is_superuser
