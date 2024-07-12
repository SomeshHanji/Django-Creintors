import django_filters
from job.models import Job
from company.models import City, State

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    salary = django_filters.NumberFilter(field_name='salary', lookup_expr='gte')
    city = django_filters.ModelChoiceFilter(queryset=City.objects.all())
    state = django_filters.ModelChoiceFilter(queryset=State.objects.all())

    class Meta:
        model = Job
        fields = ['title', 'salary', 'city', 'state']
