import django_filters

from .models import Journal

    
class JournalFilter(django_filters.FilterSet):
    class Meta:
        model = Journal
        fields = [
           'date_def',
           'name_asu',
           'module_type',
           'module_type_mkc',
           'fault',
           'events',
        ]
