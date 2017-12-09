from django import forms
# from django.forms.formsets import BaseFormSet
# from django.forms.models import modelformset_factory
from .models import RoleObject, LogicalGroupObject


class RoleCreateForm(forms.ModelForm):
    class Meta:
        model = RoleObject
        fields = [
            'shortname',
            'exid',
        ]

    def __init__(self, owner=None, *args, **kwargs):
        super(RoleCreateForm, self).__init__(*args, **kwargs)


class LogicalGroupCreateForm(forms.ModelForm):
    class Meta:
        model = LogicalGroupObject
        fields = [
            'shortname',
            'exid',
        ]

    def __init__(self, owner=None, *args, **kwargs):
        super(LogicalGroupCreateForm, self).__init__(*args, **kwargs)


class ConfigSectionCreateForm(forms.ModelForm):
    class Meta:
        model = LogicalGroupObject
        fields = [
            'shortname',
            'exid',
        ]

    def __init__(self, owner=None, *args, **kwargs):
        super(ConfigSectionCreateForm, self).__init__(*args, **kwargs)