from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, TemplateView
from .forms import RoleCreateForm, LogicalGroupCreateForm, ConfigSectionCreateForm
from .models import RoleObject, LogicalGroupObject, ConfigSectionObject

# Create your views here.
class HomeView(TemplateView):
    """ Simple Template View"""
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class DevView(TemplateView):
    """ Simple Template View"""
    template_name = 'dev.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DevView, self).get_context_data(**kwargs)
        return context


class RoleListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return RoleObject.objects.filter(owner=self.request.user)


class RoleDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RoleObject.objects.filter(owner=self.request.user)


class RoleCreateView(LoginRequiredMixin, CreateView):
    form_class = RoleCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RoleCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RoleCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Role'
        return context

    def get_form_kwargs(self):
        kwargs = super(RoleCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class RoleUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RoleCreateForm
    template_name = 'extender/roleobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RoleUpdateView, self).get_context_data(*args, **kwargs)
        shortname = self.get_object().shortname
        context['title'] = f'Update Name: {shortname}'
        return context

    def get_queryset(self):
        return RoleObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(RoleUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class LogicalGroupListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return LogicalGroupObject.objects.filter(owner=self.request.user)


class LogicalGroupDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return LogicalGroupObject.objects.filter(owner=self.request.user)


class LogicalGroupCreateView(LoginRequiredMixin, CreateView):
    form_class = LogicalGroupCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(LogicalGroupCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(LogicalGroupCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create LogicalGroup'
        return context

    def get_form_kwargs(self):
        kwargs = super(LogicalGroupCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class LogicalGroupUpdateView(LoginRequiredMixin, UpdateView):
    form_class = LogicalGroupCreateForm
    template_name = 'extender/logicalgroupobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LogicalGroupUpdateView, self).get_context_data(*args, **kwargs)
        shortname = self.get_object().shortname
        context['title'] = f'Update Name: {shortname}'
        return context

    def get_queryset(self):
        return LogicalGroupObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(LogicalGroupUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ConfigSectionListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return ConfigSectionObject.objects.filter(owner=self.request.user)


class ConfigSectionDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return ConfigSectionObject.objects.filter(owner=self.request.user)


class ConfigSectionCreateView(LoginRequiredMixin, CreateView):
    form_class = ConfigSectionCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ConfigSectionCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ConfigSectionCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create ConfigSection'
        return context

    def get_form_kwargs(self):
        kwargs = super(ConfigSectionCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ConfigSectionUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ConfigSectionCreateForm
    template_name = 'extender/configsectionobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ConfigSectionUpdateView, self).get_context_data(*args, **kwargs)
        shortname = self.get_object().shortname
        context['title'] = f'Update Name: {shortname}'
        return context

    def get_queryset(self):
        return ConfigSectionObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ConfigSectionUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs

