from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    login_url = '/users/login/'


class TaskDetailView(LoginRequiredMixin, DetailView):
    login_url = '/users/login/'
    model = Task


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy('task-list')
    login_url = '/users/login/'
    fields = ['title', 'description', 'due_date', 'priority', 'is_complete']

    def get_form(self):
        form = super().get_form()
        form.fields['due_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Associate the task with the current user
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('task-list')
    login_url = '/users/login/'
    fields = ['title', 'description', 'due_date', 'priority', 'is_complete']

    def get_form(self):
        form = super().get_form()
        form.fields['due_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Associate the task with the current user
        return super().form_valid(form)


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')
    login_url = '/users/login/'
