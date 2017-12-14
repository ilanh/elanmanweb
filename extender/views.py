from django.contrib.auth.mixins import LoginRequiredMixin
import hmac
import subprocess
# import os
from hashlib import sha1
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.encoding import force_bytes
import requests
from ipaddress import ip_address, ip_network
from django import template
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .forms import (
    RoleCreateForm, 
    LogicalGroupCreateForm, 
    ConfigSectionCreateForm, 
    RoleTaskCreateForm, 
    ApiCreateForm, 
    ApiSectionCreateForm,
    ApiSubCreateForm,
    ConfigSubCreateForm,
    RoleTemplateCreateForm,
    ConfigValueCreateForm,
    ApiValueCreateForm,
)
from .models import (
    RoleObject, 
    LogicalGroupObject, 
    ConfigSectionObject, 
    RoleTaskObject, 
    ApiObject, 
    ApiSectionObject,
    ApiSubObject,
    ConfigSubObject,
    RoleTemplateObject,
    ConfigValueObject,
    ApiValueObject,
)

# Create your views here.

register = template.Library()


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
        context['rolelist'] = RoleObject.objects.filter(owner=self.request.user)| \
                              RoleObject.objects.filter(ispublic=True)
        context['logicalgrouplist'] = LogicalGroupObject.objects.filter(owner=self.request.user)| \
                                      LogicalGroupObject.objects.filter(ispublic=True)
        context['configsectionlist'] = ConfigSectionObject.objects.filter(owner=self.request.user) | \
                                       ConfigSectionObject.objects.filter(ispublic=True)
        context['roletasklist'] = RoleTaskObject.objects.filter(owner=self.request.user) | \
                                  RoleTaskObject.objects.filter(ispublic=True)
        context['roletemplatelist'] = RoleTemplateObject.objects.filter(owner=self.request.user) | \
                                      RoleTemplateObject.objects.filter(ispublic=True)
        context['configobjectlist'] = ConfigSubObject.objects.filter(owner=self.request.user) | \
                                      ConfigSubObject.objects.filter(ispublic=True)
        context['configvaluelist'] = ConfigValueObject.objects.filter(owner=self.request.user) | \
                                     ConfigValueObject.objects.filter(ispublic=True)
        context['apilist'] = ApiObject.objects.filter(owner=self.request.user) | \
                             ApiObject.objects.filter(ispublic=True)
        context['apisectionlist'] = ApiSectionObject.objects.filter(owner=self.request.user) | \
                                    ApiSectionObject.objects.filter(ispublic=True)
        context['apiobjectlist'] = ApiSubObject.objects.filter(owner=self.request.user) | \
                                   ApiSubObject.objects.filter(ispublic=True)
        context['apivaluelist'] = ApiValueObject.objects.filter(owner=self.request.user) | \
                                  ApiValueObject.objects.filter(ispublic=True)
        return context


@require_POST
@csrf_exempt
def hello(request):
    # Verify if request came from GitHub
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')

    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')

    # If request reached this point we are in a good shape
    # Process the GitHub events
    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')

    if event == 'ping':
        return HttpResponse('pong')
    elif event == 'push':
        r = subprocess.call('$HOME/bin/post-receive', shell=True)
        return HttpResponse('success' + ' is' + r)

    # In case we receive an event that's not ping or push
    return HttpResponse(status=204)


class RoleListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        combined_queryset = RoleObject.objects.filter(owner=self.request.user) | \
                            RoleObject.objects.filter(ispublic=True)
        return combined_queryset


class RoleDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = RoleObject.objects.filter(owner=self.request.user) | \
                            RoleObject.objects.filter(ispublic=True)
        return combined_queryset

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
        combined_queryset = LogicalGroupObject.objects.filter(owner=self.request.user) | \
                            LogicalGroupObject.objects.filter(ispublic=True)
        return combined_queryset


class LogicalGroupDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = LogicalGroupObject.objects.filter(owner=self.request.user) | \
                            LogicalGroupObject.objects.filter(ispublic=True)
        return combined_queryset


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
        combined_queryset = ConfigSectionObject.objects.filter(owner=self.request.user) | \
                            ConfigSectionObject.objects.filter(ispublic=True)
        return combined_queryset


class ConfigSectionDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = ConfigSectionObject.objects.filter(owner=self.request.user) | \
                            ConfigSectionObject.objects.filter(ispublic=True)
        return combined_queryset


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


class RoleTaskListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        combined_queryset = RoleTaskObject.objects.filter(owner=self.request.user) | \
                            RoleTaskObject.objects.filter(ispublic=True)
        return combined_queryset


class RoleTaskDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = RoleTaskObject.objects.filter(owner=self.request.user) | \
                            RoleTaskObject.objects.filter(ispublic=True)
        return combined_queryset


class RoleTaskCreateView(LoginRequiredMixin, CreateView):
    form_class = RoleTaskCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RoleTaskCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RoleTaskCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create RoleTask'
        return context

    def get_form_kwargs(self):
        kwargs = super(RoleTaskCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class RoleTaskUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RoleTaskCreateForm
    template_name = 'extender/roletaskobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RoleTaskUpdateView, self).get_context_data(*args, **kwargs)
        shortname = self.get_object().shortname
        context['title'] = f'Update Name: {shortname}'
        return context

    def get_queryset(self):
        return RoleTaskObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(RoleTaskUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs
    
    
class ApiListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        combined_queryset = ApiObject.objects.filter(owner=self.request.user) | \
                            ApiObject.objects.filter(ispublic=True)
        return combined_queryset


class ApiDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = ApiObject.objects.filter(owner=self.request.user) | \
                            ApiObject.objects.filter(ispublic=True)
        return combined_queryset


class ApiCreateView(LoginRequiredMixin, CreateView):
    form_class = ApiCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ApiCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ApiCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Api'
        return context

    def get_form_kwargs(self):
        kwargs = super(ApiCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ApiUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ApiCreateForm
    template_name = 'extender/apiobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ApiUpdateView, self).get_context_data(*args, **kwargs)
        shortname = self.get_object().shortname
        context['title'] = f'Update Name: {shortname}'
        return context

    def get_queryset(self):
        return ApiObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ApiUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs
    
    
class ApiSectionListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        combined_queryset = ApiSectionObject.objects.filter(owner=self.request.user) | \
                            ApiSectionObject.objects.filter(ispublic=True)
        return combined_queryset


class ApiSectionDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = ApiSectionObject.objects.filter(owner=self.request.user) | \
                            ApiSectionObject.objects.filter(ispublic=True)
        return combined_queryset


class ApiSectionCreateView(LoginRequiredMixin, CreateView):
    form_class = ApiSectionCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ApiSectionCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ApiSectionCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create ApiSection'
        return context

    def get_form_kwargs(self):
        kwargs = super(ApiSectionCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ApiSectionUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ApiSectionCreateForm
    template_name = 'extender/apisectionobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ApiSectionUpdateView, self).get_context_data(*args, **kwargs)
        shortname = self.get_object().shortname
        context['title'] = f'Update Name: {shortname}'
        return context

    def get_queryset(self):
        return ApiSectionObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ApiSectionUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs
    

class ConfigSubListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        combined_queryset = ConfigSubObject.objects.filter(owner=self.request.user) | \
                            ConfigSubObject.objects.filter(ispublic=True)
        return combined_queryset


class ConfigSubDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = ConfigSubObject.objects.filter(owner=self.request.user) | \
                            ConfigSubObject.objects.filter(ispublic=True)
        return combined_queryset


class ConfigSubCreateView(LoginRequiredMixin, CreateView):
    form_class = ConfigSubCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ConfigSubCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ConfigSubCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create ConfigSub'
        return context

    def get_form_kwargs(self):
        kwargs = super(ConfigSubCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ConfigSubUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ConfigSubCreateForm
    template_name = 'extender/configsubobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ConfigSubUpdateView, self).get_context_data(*args, **kwargs)
        shortname = self.get_object().shortname
        context['title'] = f'Update Name: {shortname}'
        return context

    def get_queryset(self):
        return ConfigSubObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ConfigSubUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ApiSubListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        combined_queryset = ApiSubObject.objects.filter(owner=self.request.user) | \
                            ApiSubObject.objects.filter(ispublic=True)
        return combined_queryset


class ApiSubDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = ApiSubObject.objects.filter(owner=self.request.user) | \
                            ApiSubObject.objects.filter(ispublic=True)
        return combined_queryset


class ApiSubCreateView(LoginRequiredMixin, CreateView):
    form_class = ApiSubCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ApiSubCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ApiSubCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create ApiSub'
        return context

    def get_form_kwargs(self):
        kwargs = super(ApiSubCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ApiSubUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ApiSubCreateForm
    template_name = 'extender/apisubobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ApiSubUpdateView, self).get_context_data(*args, **kwargs)
        shortname = self.get_object().shortname
        context['title'] = f'Update Name: {shortname}'
        return context

    def get_queryset(self):
        return ApiSubObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ApiSubUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class RoleTemplateListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        combined_queryset = RoleTemplateObject.objects.filter(owner=self.request.user) | \
                            RoleTemplateObject.objects.filter(ispublic=True)
        return combined_queryset


class RoleTemplateDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = RoleTemplateObject.objects.filter(owner=self.request.user) | \
                            RoleTemplateObject.objects.filter(ispublic=True)
        return combined_queryset


class RoleTemplateCreateView(LoginRequiredMixin, CreateView):
    form_class = RoleTemplateCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RoleTemplateCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RoleTemplateCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create RoleTemplate'
        return context

    def get_form_kwargs(self):
        kwargs = super(RoleTemplateCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class RoleTemplateUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RoleTemplateCreateForm
    template_name = 'extender/roletemplateobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RoleTemplateUpdateView, self).get_context_data(*args, **kwargs)
        shortname = self.get_object().shortname
        context['title'] = f'Update Name: {shortname}'
        return context

    def get_queryset(self):
        return RoleTemplateObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(RoleTemplateUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ConfigValueListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        combined_queryset = ConfigValueObject.objects.filter(owner=self.request.user) | \
                            ConfigValueObject.objects.filter(ispublic=True)
        return combined_queryset


class ConfigValueDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = ConfigValueObject.objects.filter(owner=self.request.user) | \
                            ConfigValueObject.objects.filter(ispublic=True)
        return combined_queryset


class ConfigValueCreateView(LoginRequiredMixin, CreateView):
    form_class = ConfigValueCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ConfigValueCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ConfigValueCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create ConfigValue'
        return context

    def get_form_kwargs(self):
        kwargs = super(ConfigValueCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ConfigValueUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ConfigValueCreateForm
    template_name = 'extender/configvalueobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ConfigValueUpdateView, self).get_context_data(*args, **kwargs)
        exid = self.get_object().exid
        context['title'] = f'Update Name: {exid}'
        return context

    def get_queryset(self):
        return ConfigValueObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ConfigValueUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ApiValueListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        combined_queryset = ApiValueObject.objects.filter(owner=self.request.user) | \
                            ApiValueObject.objects.filter(ispublic=True)
        return combined_queryset


class ApiValueDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        combined_queryset = ApiValueObject.objects.filter(owner=self.request.user) | \
                            ApiValueObject.objects.filter(ispublic=True)
        return combined_queryset


class ApiValueCreateView(LoginRequiredMixin, CreateView):
    form_class = ApiValueCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ApiValueCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ApiValueCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create ApiValue'
        return context

    def get_form_kwargs(self):
        kwargs = super(ApiValueCreateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ApiValueUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ApiValueCreateForm
    template_name = 'extender/apivalueobject_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ApiValueUpdateView, self).get_context_data(*args, **kwargs)
        exid = self.get_object().exid
        context['title'] = f'Update Name: {exid}'
        return context

    def get_queryset(self):
        return ApiValueObject.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ApiValueUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


