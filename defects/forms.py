from django import forms
from .models import Journal


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
            'number_module_mkc',
            'number_cannel_mkc',
            'channel_purpose',
            'fault',
            'author_def',
            #'date_events'         
        ]      

        widgets = {
            'date_def': forms.DateInput(attrs={'type': 'date'}),
            #'date_events': forms.DateInput(attrs={'type': 'date'}),
        }


class JournalFormEvent(forms.ModelForm):
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
            'number_module_mkc',
            'number_cannel_mkc',
            'channel_purpose',
            'fault',
            'author_def',
            'events',
            'date_events',
            'author_events',
        ]      

        widgets = {
           # 'date_def': forms.DateInput(attrs={'type': 'date'}),
           'date_events': forms.DateInput(attrs={'type': 'date'}),
        }

class JournalFormEventTwo(forms.ModelForm):
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
            'number_module_mkc',
            'number_cannel_mkc',
            'channel_purpose',
            'fault',
            'author_def',
            'events',
            'date_events',
            'author_events',
            'events_two',
            'date_events_two',
            'author_events_two'
        ]      

        widgets = {
           # 'date_def': forms.DateInput(attrs={'type': 'date'}),
           # 'date_events': forms.DateInput(attrs={'type': 'date'}),
            'date_events_two': forms.DateInput(attrs={'type': 'date'}),
        }