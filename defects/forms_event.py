from django import forms
from .models import Journal


# class JournalForm(forms.ModelForm):
#     class Meta:
#         model = Journal
#         fields =  [  #'__all__'
       
#             'date_def',
#             'name_asu',
#             'number_cabinet',
#             'module_type',
#             'number_module',
#             'number_cannel',
#             'module_type_mkc',
#             'number_cannel_mkc',
#             'channel_purpose',
#             'fault',
#             'author_def',
#         ]      

#         widgets = {
#             'date_def': forms.DateInput(attrs={'type': 'date'}),
#             'date_events': forms.DateInput(attrs={'type': 'date'}),
#         }


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields =  [  #'__all__'
       
            'date_def',
            'name_asu',
            'number_cabinet',
            'module_type',
            'number_module',
            'number_cannel',
            'module_type_mkc',
            'number_cannel_mkc',
            'channel_purpose',
            'fault',
            'author_def',
            'events',
            'date_events',
            'author_events',
        ]      

        widgets = {
            'date_def': forms.DateInput(attrs={'type': 'date'}),
            'date_events': forms.DateInput(attrs={'type': 'date'}),
        }