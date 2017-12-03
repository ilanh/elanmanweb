from django import forms
from django.forms.formsets import formset_factory


class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)


class ContactForm2(forms.Form):
    message = forms.CharField(max_length=100)


class ContactForm3(forms.Form):
    sender = forms.CharField(max_length=100)


Contact1Formset = formset_factory(ContactForm2, extra=8, max_num=5)


class RegionForm(forms.Form):
    shortname = forms.CharField(max_length=16)
    desc = forms.CharField(max_length=64)
    exid = forms.CharField(max_length=8)


class RoleForm(forms.Form):
    shortname = forms.CharField(max_length=16)
    desc = forms.CharField(max_length=64)
    exid = forms.CharField(max_length=8)
    isaddon = forms.BooleanField(required=False)


class BrandForm(forms.Form):
    shortname = forms.CharField(max_length=16)
    desc = forms.CharField(max_length=64)
    domain = forms.CharField(max_length=32)
    exid = forms.CharField(max_length=8)

class ServerNodeForm(forms.Form):
    fullname = forms.CharField(max_length=32)
    role = forms.CharField(max_length=16)
    brand = forms.CharField(max_length=16)
    logicalgroup = forms.CharField(max_length=16)

RegionFormset = formset_factory(RegionForm, extra=2, max_num=3)

RoleFormset = formset_factory(RoleForm, extra=4, max_num=8)

BrandFormset = formset_factory(BrandForm, extra=2, max_num=8)

ServerNodeFormset = formset_factory(ServerNodeForm, extra=2, max_num=16)
