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
]