from django import forms
from django.utils.translation import gettext_lazy as _
# from django.forms.formsets import BaseFormSet
# from django.forms.models import modelformset_factory
from .models import RoleObject, LogicalGroupObject, ConfigSectionObject, RoleTaskObject, ApiObject, ApiSectionObject


class RoleCreateForm(forms.ModelForm):
    class Meta:
        model = RoleObject
        fields = [
            'shortname',
            'exid',
        ]
        labels = {
            'shortname': _('Short Name'),
            'exid': _('External ID'),
        }
        help_texts = {
            'shortname': _('Directory name for that role'),
            'exid': _('Key to link yaml vars'),
        }
        error_messages = {
            'name': {
                'max_length': _("Name is too long."),
            },
            'exid': {
                'max_length': _("ID is too long."),
            },
        }

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
        model = ConfigSectionObject
        fields = [
            'shortname',
            'exid',
            'desc',
            'listobject',
        ]

    def __init__(self, owner=None, *args, **kwargs):
        super(ConfigSectionCreateForm, self).__init__(*args, **kwargs)


class RoleTaskCreateForm(forms.ModelForm):
    class Meta:
        model = RoleTaskObject
        fields = [
            'shortname',
            'role',
            'desc',
        ]

    def __init__(self, owner=None, *args, **kwargs):
        super(RoleTaskCreateForm, self).__init__(*args, **kwargs)


class ApiCreateForm(forms.ModelForm):
    class Meta:
        model = ApiObject
        fields = [
            'shortname',
            'desc',
        ]

    def __init__(self, owner=None, *args, **kwargs):
        super(ApiCreateForm, self).__init__(*args, **kwargs)


class ApiSectionCreateForm(forms.ModelForm):
    class Meta:
        model = ApiSectionObject
        fields = [
            'shortname',
            'exid',
            'api',
            'desc',
        ]

    def __init__(self, owner=None, *args, **kwargs):
        super(ApiSectionCreateForm, self).__init__(*args, **kwargs)