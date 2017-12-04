from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        print(context)
        return context