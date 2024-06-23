import django_filters
from job.models import Job
from company.models import City, State

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    salary = django_filters.NumberFilter(field_name='salary', lookup_expr='gte')
    city = django_filters.CharFilter(field_name='city__name', lookup_expr='icontains')
    state = django_filters.CharFilter(field_name='city__state__name', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['title', 'salary', 'city', 'state']