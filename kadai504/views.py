from kadai504.models import Fruits
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Fruits
from .forms import FruitsForm

# Create your views here.

class IndexView(generic.ListView):
    model = Fruits
    template_name = 'fruits/index.html'


class CreateView(generic.edit.CreateView):
    model = Fruits
    # form = FruitsForm()
    fields = ('no', 'name', 'memo')
    template_name = 'fruits/create.html'
    success_url = "/fruits/"


class DetailView(generic.DetailView):
    model = Fruits
    fields = ('no', 'name', 'memo')
    template_name = 'fruits/detail.html'


class DeleteView(generic.edit.DeleteView):
    model = Fruits
    template_name = 'fruits/delete.html'
    success_url = reverse_lazy('fruits:index')


class UpdateView(generic.edit.UpdateView):
    model = Fruits
    fields = ('no', 'name', 'memo')
    template_name = 'fruits/update.html'