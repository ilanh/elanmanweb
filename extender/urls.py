""" urls under /dev/ space """

from django.conf.urls import url
from .views import (
    RoleDetailView,
    RoleCreateView,
    RoleUpdateView,
    RoleListView,
    DevView,
    LogicalGroupCreateView,
    LogicalGroupDetailView,
    LogicalGroupUpdateView,
    LogicalGroupListView,
    ConfigSectionCreateView,
    ConfigSectionDetailView,
    ConfigSectionUpdateView,
    ConfigSectionListView,
    RoleTaskCreateView,
    RoleTaskDetailView,
    RoleTaskUpdateView,
    RoleTaskListView,
)


urlpatterns = [
    url(r'^$', DevView.as_view(), name='index'),
    url(r'^role/create/$', RoleCreateView.as_view(), name='createrole'),
    url(r'^role/(?P<slug>[\w-]+)/$', RoleDetailView.as_view(), name='getrole'),
    url(r'^role/(?P<slug>[\w-]+)/edit/$', RoleUpdateView.as_view(), name='editrole'),
    url(r'^role/$', RoleListView.as_view(), name='listrole'),
    url(r'^logicalgroup/create/$', LogicalGroupCreateView.as_view(), name='createlogicalgroup'),
    url(r'^logicalgroup/(?P<slug>[\w-]+)/$', LogicalGroupDetailView.as_view(), name='getlogicalgroup'),
    url(r'^logicalgroup/(?P<slug>[\w-]+)/edit/$', LogicalGroupUpdateView.as_view(), name='editlogicalgroup'),
    url(r'^logicalgroup/$', LogicalGroupListView.as_view(), name='listlogicalgroup'),
    url(r'^configsection/create/$', ConfigSectionCreateView.as_view(), name='createconfigsection'),
    url(r'^configsection/(?P<slug>[\w-]+)/$', ConfigSectionDetailView.as_view(), name='getconfigsection'),
    url(r'^configsection/(?P<slug>[\w-]+)/edit/$', ConfigSectionUpdateView.as_view(), name='editconfigsection'),
    url(r'^configsection/$', ConfigSectionListView.as_view(), name='listconfigsection'),
    url(r'^roletask/create/$', RoleTaskCreateView.as_view(), name='createroletask'),
    url(r'^roletask/(?P<slug>[\w-]+)/$', RoleTaskDetailView.as_view(), name='getroletask'),
    url(r'^roletask/(?P<slug>[\w-]+)/edit/$', RoleTaskUpdateView.as_view(), name='editroletask'),
    url(r'^roletask/$', RoleTaskListView.as_view(), name='listroletask'),
]