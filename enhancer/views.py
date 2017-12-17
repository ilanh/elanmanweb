# from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView
from .models import PublicContrib
# Create your views here.


class PublicContribListView(ListView):
    def get_queryset(self):
        combined_queryset = PublicContrib.objects.filter(owner=self.request.user) | \
                            PublicContrib.objects.filter(ispublic=True)
        return combined_queryset