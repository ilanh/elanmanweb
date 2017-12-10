from django import forms
from django.forms.formsets import formset_factory
from extender.models import RoleObject, LogicalGroupObject, ConfigValueObject, ApiValueObject


class RegionForm(forms.Form):
    shortname = forms.CharField(max_length=16)
    desc = forms.CharField(max_length=64)
    exid = forms.CharField(max_length=8)


class BrandForm(forms.Form):
    shortname = forms.CharField(max_length=16)
    desc = forms.CharField(max_length=64)
    domain = forms.CharField(max_length=32)
    exid = forms.CharField(max_length=8)


class ServerNodeForm(forms.Form):
    fullname = forms.CharField(max_length=32)
    role = forms.ChoiceField(choices=[(str(x.exid), str(x.shortname)) for x in RoleObject.objects.all()])
    brand = forms.ChoiceField(choices=['a1','b2'])
    region = forms.ChoiceField(choices=['a1', 'b2'])
    logicalgroup = forms.ChoiceField(choices=[(str(x.exid), str(x.shortname)) for x in LogicalGroupObject.objects.all()])


class ConfigLevelForm(forms.Form):
    value = forms.ChoiceField(choices=[(str(x.exid), str(x.desc)) for x in ConfigValueObject.objects.all()])
    role = forms.ChoiceField(choices=[(str(x.exid), str(x.shortname)) for x in RoleObject.objects.all()])
    brand = forms.ChoiceField(choices=['a1', 'b2'])
    region = forms.ChoiceField(choices=['a1', 'b2'])
    logicalgroup = forms.ChoiceField(
        choices=[(str(x.exid), str(x.shortname)) for x in LogicalGroupObject.objects.all()])


class ApiLevelForm(forms.Form):
    value = forms.ChoiceField(choices=[(str(x.exid), str(x.desc)) for x in ApiValueObject.objects.all()])
    role = forms.ChoiceField(choices=[(str(x.exid), str(x.shortname)) for x in RoleObject.objects.all()])
    brand = forms.ChoiceField(choices=['a1', 'b2'])
    region = forms.ChoiceField(choices=['a1', 'b2'])
    logicalgroup = forms.ChoiceField(
        choices=[(str(x.exid), str(x.shortname)) for x in LogicalGroupObject.objects.all()])


RegionFormset = formset_factory(RegionForm, extra=1, min_num=1)

BrandFormset = formset_factory(BrandForm, extra=1, min_num=1)

ServerNodeFormset = formset_factory(ServerNodeForm, extra=1, min_num=1)

ConfigLevelFormset = formset_factory(ConfigLevelForm, extra=1, min_num=1)

ApiLevelFormset = formset_factory(ApiLevelForm, extra=1, min_num=1)

