from django import forms
from django.conf import settings
from django.forms.formsets import formset_factory
from extender.models import RoleObject, LogicalGroupObject, ConfigValueObject, ApiValueObject

User = settings.AUTH_USER_MODEL

class RegionForm(forms.Form):
    shortname = forms.CharField(max_length=16)
    desc = forms.CharField(max_length=64)
    exid = forms.CharField(max_length=8)


class BrandForm(forms.Form):
    shortname = forms.CharField(max_length=16)
    desc = forms.CharField(max_length=64)
    # domain = forms.CharField(max_length=32)
    exid = forms.CharField(max_length=8)


class ServerNodeForm(forms.Form):
    fullname = forms.CharField(max_length=32)
    role = forms.ChoiceField(choices=[(str(x.exid), str(x.shortname)) for x in RoleObject.objects.filter(addon=False, ispublic=True)])
    brand = forms.ChoiceField(choices=['a1','b2'])
    region = forms.ChoiceField(choices=['a1', 'b2'])
    logicalgroup = forms.ChoiceField(
        choices=[(str(x.exid), str(x.shortname)) for x in LogicalGroupObject.objects.filter(ispublic=True)])


class ConfigLevelForm(forms.Form):
    value = forms.ChoiceField(
        choices=[(str(x.exid), str(x.desc)) for x in ConfigValueObject.objects.filter(ispublic=True)])
    role = forms.MultipleChoiceField(
        choices=[(str(x.exid), str(x.shortname)) for x in RoleObject.objects.filter(ispublic=True)],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    brand = forms.MultipleChoiceField(
        choices=['a1', 'b2'],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    region = forms.MultipleChoiceField(
        choices=['a1', 'b2'],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    logicalgroup = forms.MultipleChoiceField(
        choices=[(str(x.exid), str(x.shortname)) for x in LogicalGroupObject.objects.filter(ispublic=True)],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class ApiLevelForm(forms.Form):
    value = forms.ChoiceField(choices=[(str(x.exid), str(x.desc)) for x in ApiValueObject.objects.filter(ispublic=True)])
    role = forms.MultipleChoiceField(
        choices=[(str(x.exid), str(x.shortname)) for x in RoleObject.objects.filter(ispublic=True)],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    brand = forms.MultipleChoiceField(
        choices=['a1', 'b2'],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    region = forms.MultipleChoiceField(
        choices=['a1', 'b2'],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    logicalgroup = forms.MultipleChoiceField(
        choices=[(str(x.exid), str(x.shortname)) for x in LogicalGroupObject.objects.filter(ispublic=True)],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


RegionFormset = formset_factory(RegionForm, extra=1, min_num=1)

BrandFormset = formset_factory(BrandForm, extra=1, min_num=1)

ServerNodeFormset = formset_factory(ServerNodeForm, extra=1, min_num=1)

ConfigLevelFormset = formset_factory(ConfigLevelForm, extra=1, min_num=1)

ApiLevelFormset = formset_factory(ApiLevelForm, extra=1, min_num=1)

