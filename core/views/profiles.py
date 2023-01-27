from django.views.generic import DetailView
from ..models.profile import Profile


class ProfileDetailView(DetailView):
    model = Profile
