""" urls under /dev/ space """

from django.conf.urls import url
from .views import RoleDetailView, RoleCreateView, RoleUpdateView, RoleListView

urlpatterns = [
    url(r'^role/(?P<slug>[\w-]+)/get/$', RoleDetailView.as_view(), name='getrole'),
    url(r'^role/(?P<slug>[\w-]+)/edit/$', RoleUpdateView.as_view(), name='editrole'),
    url(r'^role/create/$', RoleCreateView.as_view(), name='createrole'),
    url(r'^role/list/$', RoleListView.as_view(), name='listrole'),
]