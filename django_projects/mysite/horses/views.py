from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from horses.models import Horse, Breed

# Create your views here.
class HorseList(LoginRequiredMixin, View):
    def get(self, request):
        breed = Breed.objects.all().count()
        all = Horse.objects.all()
        ctx = {'breed_count': breed, 'horse_list': all}
        return render(request, 'horses/horse_list.html', ctx)

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breed = Breed.objects.all()
        ctx = {'breed_list': breed}
        return render(request, 'horses/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('horses:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('horses:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('horses:all')

class HorseCreate(LoginRequiredMixin, CreateView):
    model = Horse
    fields = '__all__'
    success_url = reverse_lazy('horses:all')

class HorseUpdate(LoginRequiredMixin, UpdateView):
    model = Horse
    fields = '__all__'
    success_url = reverse_lazy('horses:all')

class HorseDelete(LoginRequiredMixin, DeleteView):
    model = Horse
    fields = '__all__'
    success_url = reverse_lazy('horses:all')
