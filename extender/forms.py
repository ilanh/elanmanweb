from django import forms
from django.utils.translation import gettext_lazy as _
# from django.forms.formsets import BaseFormSet
# from django.forms.models import modelformset_factory
from .models import (
    RoleObject,
    LogicalGroupObject,
    ConfigSectionObject,
    RoleTaskObject,
    ApiObject,
    ApiSectionObject,
    ApiSubObject,
    RoleTemplateObject,
    ConfigSubObject,
    ConfigValueObject,
    ApiValueObject,
)


class RoleCreateForm(forms.ModelForm):
    class Meta:
        model = RoleObject
        fields = [
            'shortname',
            'desc',
            'exid',
        ]
        labels = {
            'shortname': _('Short Name'),
            'desc': _('description'),
            'exid': _('External ID'),
        }
        help_texts = {
            'shortname': _('Directory name for that role'),
            'exid': _('Key to link yaml vars'),
        }
        error_messages = {
            'shortname': {
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
        labels = {
            'shortname': _('Short Name'),
            'exid': _('External ID'),
        }
        help_texts = {
            'shortname': _('File name for that Group'),
            'exid': _('Key to link yaml vars'),
        }
        error_messages = {
            'shortname': {
                'max_length': _("Name is too long."),
            },
            'exid': {
                'max_length': _("ID is too long."),
            },
        }

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
        labels = {
            'shortname': _('Short Name'),
            'exid': _('External ID'),
            'desc': _('Description'),
            'listobject': _('Is this section a list'),
        }
        help_texts = {
            'shortname': _('Section name in yaml file'),
            'exid': _('Key to link yaml vars'),
            'desc': _('Description'),
            'listobject': _('When constructed in yaml, is it a list'),
        }
        error_messages = {
            'shortname': {
                'max_length': _("Name is too long."),
            },
            'exid': {
                'max_length': _("ID is too long."),
            },
        }

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
        labels = {
            'shortname': _('Task Name'),
            'role': _('Assigned to role'),
            'desc': _('Description'),
        }
        help_texts = {
            'shortname': _('Task file name, without ext'),
            'role': _('Choose a role that this task file will be copied to'),
            'desc': _('Task description'),
        }
        error_messages = {
            'shortname': {
                'max_length': _("Name is too long."),
            },
            'exid': {
                'max_length': _("ID is too long."),
            },
        }

    def __init__(self, owner=None, *args, **kwargs):
        super(RoleTaskCreateForm, self).__init__(*args, **kwargs)


class ApiCreateForm(forms.ModelForm):
    class Meta:
        model = ApiObject
        fields = [
            'shortname',
            'desc',
        ]
        labels = {
            'shortname': _('Short Name'),
            'desc': _('Description'),
        }
        help_texts = {
            'shortname': _('API name '),
            'desc': _('Description for that API'),
        }
        error_messages = {
            'shortname': {
                'max_length': _("Name is too long."),
            },
            'desc': {
                'max_length': _("ID is too long."),
            },
        }

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
        labels = {
            'shortname': _('Section Name'),
            'exid': _('External ID'),
            'desc': _('Description'),
            'api': _('API'),
        }
        help_texts = {
            'shortname': _('First part of API command'),
            'exid': _('Key to link yaml vars'),
            'desc': _('Section description'),
            'api': _('Parent API'),
        }
        error_messages = {
            'shortname': {
                'max_length': _("Name is too long."),
            },
            'desc': {
                'max_length': _("ID is too long."),
            },
        }

    def __init__(self, owner=None, *args, **kwargs):
        super(ApiSectionCreateForm, self).__init__(*args, **kwargs)


class ApiSubCreateForm(forms.ModelForm):
    class Meta:
        model = ApiSubObject
        fields = [
            'shortname',
            'exid',
            'section',
            'desc',
        ]
        labels = {
            'shortname': _('Sub object Name'),
            'exid': _('External ID'),
            'desc': _('Description'),
            'section': _('API Section'),
        }
        help_texts = {
            'shortname': _('Second part of API command'),
            'exid': _('Key to link yaml vars'),
            'desc': _('Sub Object description'),
            'section': _('Section for this object'),
        }
        error_messages = {
            'name': {
                'max_length': _("Name is too long."),
            },
            'desc': {
                'max_length': _("ID is too long."),
            },
        }

    def __init__(self, owner=None, *args, **kwargs):
        super(ApiSubCreateForm, self).__init__(*args, **kwargs)


class RoleTemplateCreateForm(forms.ModelForm):
    class Meta:
        model = RoleTemplateObject
        fields = [
            'shortname',
            'role',
            'desc',
            'istemplate',
        ]
        labels = {
            'shortname': _('Template Name'),
            'role': _('Role'),
            'desc': _('Description'),
            'istemplate': _('Parse'),
        }
        help_texts = {
            'shortname': _('Actual template file name'),
            'role': _('Assign to role'),
            'desc': _('Template description'),
            'istemplate': _('Process Jinja2 or just copy'),
        }
        error_messages = {
            'shortname': {
                'max_length': _("Name is too long."),
            },
            'desc': {
                'max_length': _("ID is too long."),
            },
        }

    def __init__(self, owner=None, *args, **kwargs):
        super(RoleTemplateCreateForm, self).__init__(*args, **kwargs)


class ConfigSubCreateForm(forms.ModelForm):
    class Meta:
        model = ConfigSubObject
        fields = [
            'shortname',
            'exid',
            'section',
            'desc',
        ]
        labels = {
            'shortname': _('Sub object Name'),
            'exid': _('External ID'),
            'desc': _('Description'),
            'section': _('Config Section'),
        }
        help_texts = {
            'shortname': _('Config Object name'),
            'exid': _('Key to link yaml vars'),
            'desc': _('Config Object description'),
            'section': _('Section for this object'),
        }
        error_messages = {
            'name': {
                'max_length': _("Name is too long."),
            },
            'desc': {
                'max_length': _("ID is too long."),
            },
        }

    def __init__(self, owner=None, *args, **kwargs):
        super(ConfigSubCreateForm, self).__init__(*args, **kwargs)


class ConfigValueCreateForm(forms.ModelForm):
    class Meta:
        model = ConfigValueObject
        fields = [
            'exid',
            'subobject',
            'value',
            'desc',
        ]
        labels = {
            'exid': _('External ID'),
            'subobject': _('Sub object Name'),
            'value': _('Object Value'),
            'desc': _('Description'),
        }
        help_texts = {
            'exid': _('Key to link yaml vars'),
            'subobject': _('Parent Object'),
            'value': _('Value of object'),
            'desc': _('short Description'),
        }
        error_messages = {
            'name': {
                'max_length': _("Name is too long."),
            },
            'desc': {
                'max_length': _("ID is too long."),
            },
        }

    def __init__(self, owner=None, *args, **kwargs):
        super(ConfigValueCreateForm, self).__init__(*args, **kwargs)


class ApiValueCreateForm(forms.ModelForm):
    class Meta:
        model = ApiValueObject
        fields = [
            'exid',
            'subobject',
            'value',
            'desc',
        ]
        labels = {
            'exid': _('External ID'),
            'subobject': _('Sub object Name'),
            'value': _('Object Value'),
            'desc': _('Description'),
        }
        help_texts = {
            'exid': _('Key to link yaml vars'),
            'subobject': _('Parent Object'),
            'value': _('Value of object'),
            'desc': _('short Description'),
        }
        error_messages = {
            'name': {
                'max_length': _("Name is too long."),
            },
            'desc': {
                'max_length': _("ID is too long."),
            },
        }

    def __init__(self, owner=None, *args, **kwargs):
        super(ApiValueCreateForm, self).__init__(*args, **kwargs)