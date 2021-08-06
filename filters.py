from django_filters import rest_framework as filters
from apps.console.doctalk.models import Profile


class ProfileFilter(filters.FilterSet):
    dob_gt = filters.DateFilter(field_name="dob", lookup_expr="gt")
    dob_lt = filters.DateFilter(field_name="dob", lookup_expr="lt")

    class Meta:
        model = Profile
        fields = []
