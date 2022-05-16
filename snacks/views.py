from django.shortcuts import render

from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView,
                                  DetailView)
from .models import Snack
class HomeView(TemplateView):
    template_name = 'home.html'

class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack
class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields =["title", "purchaser", "description"]
class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields =["title", "description"]
class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url ='/'