from django.conf.urls import url
from .views import *

app_name = 'enhancer'

urlpatterns = [
    url(r'^$', PublicContribListView.as_view(), name='index'),
    ]